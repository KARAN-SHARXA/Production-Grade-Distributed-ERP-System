from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.stock import Stock
from app.models.stock_movement import StockMovement, StockMovementType
from app.schemas.stock import StockCreate, StockUpdate, StockResponse
from app.schemas.stock_adjustment import StockAdjustmentRequest
from app.schemas.transfer import StockTransferRequest
router = APIRouter(
    prefix="/stocks",
    tags=["Stocks"],
)


# ---------------- CREATE STOCK ----------------

@router.post("/", response_model=StockResponse, status_code=201)
async def create_stock(
    data: StockCreate,
    db: AsyncSession = Depends(get_db),
):
    stock = Stock(**data.model_dump())

    db.add(stock)
    await db.commit()
    await db.refresh(stock)

    return stock


# ---------------- GET ALL STOCK ----------------

@router.get("/", response_model=list[StockResponse])
async def get_stocks(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Stock))
    return result.scalars().all()


# ---------------- GET STOCK BY ID ----------------

@router.get("/{stock_id}", response_model=StockResponse)
async def get_stock(
    stock_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    stock = await db.get(Stock, stock_id)

    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")

    return stock


# ---------------- UPDATE STOCK ----------------

@router.put("/{stock_id}", response_model=StockResponse)
async def update_stock(
    stock_id: UUID,
    data: StockUpdate,
    db: AsyncSession = Depends(get_db),
):
    stock = await db.get(Stock, stock_id)

    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")

    update_data = data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(stock, key, value)

    await db.commit()
    await db.refresh(stock)

    return stock


# ---------------- DELETE STOCK ----------------

@router.delete("/{stock_id}")
async def delete_stock(
    stock_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    stock = await db.get(Stock, stock_id)

    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")

    await db.delete(stock)
    await db.commit()

    return {"message": "Stock deleted successfully"}


# ---------------- GET STOCK BY PRODUCT ----------------

@router.get("/product/{product_id}")
async def get_product_stock(
    product_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Stock).where(Stock.product_id == product_id)
    )

    return result.scalars().all()


# ---------------- GET STOCK BY WAREHOUSE ----------------

@router.get("/warehouse/{warehouse_id}")
async def get_warehouse_stock(
    warehouse_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Stock).where(Stock.warehouse_id == warehouse_id)
    )

    return result.scalars().all()


# ---------------- STOCK ADJUSTMENT ----------------

@router.post("/adjust")
async def adjust_stock(
    data: StockAdjustmentRequest,
    db: AsyncSession = Depends(get_db),
):
    stock = await db.get(Stock, data.stock_id)

    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")

    new_quantity = stock.quantity + data.quantity

    if new_quantity < 0:
        raise HTTPException(status_code=400, detail="Insufficient stock")

    stock.quantity = new_quantity

    movement = StockMovement(
        product_id=stock.product_id,
        warehouse_id=stock.warehouse_id,
        movement_type=StockMovementType.ADJUSTMENT.value,
        quantity=data.quantity,
        reference_id=f"ADJ-{stock.id}",
        notes=data.reason,
    )

    db.add(movement)

    await db.commit()
    await db.refresh(stock)

    return {
        "message": "Stock adjusted successfully",
        "quantity": stock.quantity,
    }

@router.post("/transfer")
async def transfer_stock(
    data: StockTransferRequest,
    db: AsyncSession = Depends(get_db),
):
    # Source stock
    result = await db.execute(
        select(Stock).where(
            (Stock.product_id == data.product_id) &
            (Stock.warehouse_id == data.from_warehouse)
        )
    )
    source = result.scalar_one_or_none()

    if not source:
        raise HTTPException(status_code=404, detail="Source stock not found")

    if source.quantity < data.quantity:
        raise HTTPException(status_code=400, detail="Insufficient stock")

    # Destination stock
    result = await db.execute(
        select(Stock).where(
            (Stock.product_id == data.product_id) &
            (Stock.warehouse_id == data.to_warehouse)
        )
    )
    destination = result.scalar_one_or_none()

    if destination is None:
        destination = Stock(
            product_id=data.product_id,
            warehouse_id=data.to_warehouse,
            quantity=0,
            reserved_quantity=0,
        )
        db.add(destination)
        await db.flush()

    # Update quantities
    source.quantity -= data.quantity
    destination.quantity += data.quantity

    # OUT movement
    db.add(
        StockMovement(
            product_id=data.product_id,
            warehouse_id=data.from_warehouse,
            movement_type=StockMovementType.TRANSFER.value,
            quantity=-data.quantity,
            reference_id=f"TR-{source.id}",
            notes=f"OUT: {data.reason}",
        )
    )

    # IN movement
    db.add(
        StockMovement(
            product_id=data.product_id,
            warehouse_id=data.to_warehouse,
            movement_type=StockMovementType.TRANSFER.value,
            quantity=data.quantity,
            reference_id=f"TR-{destination.id}",
            notes=f"IN: {data.reason}",
        )
    )

    await db.commit()
    await db.refresh(source)
    await db.refresh(destination)

    return {
        "message": "Stock transferred successfully",
        "from_quantity": source.quantity,
        "to_quantity": destination.quantity,
    }    