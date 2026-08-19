"""add roles and permissions

Revision ID: 2614cfc6c4a9
Revises: 17206b9ba565
Create Date: 2026-08-19 14:55:24.703112

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2614cfc6c4a9"
down_revision: Union[str, Sequence[str], None] = "17206b9ba565"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    # =========================
    # Create permissions table
    # =========================

    op.create_table(
        "permissions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        op.f("ix_permissions_id"),
        "permissions",
        ["id"],
        unique=False,
    )

    op.create_index(
        op.f("ix_permissions_name"),
        "permissions",
        ["name"],
        unique=True,
    )

    # =========================
    # Create roles table
    # =========================

    op.create_table(
        "roles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        op.f("ix_roles_id"),
        "roles",
        ["id"],
        unique=False,
    )

    op.create_index(
        op.f("ix_roles_name"),
        "roles",
        ["name"],
        unique=True,
    )

    # =========================
    # Create role_permissions
    # =========================

    op.create_table(
        "role_permissions",
        sa.Column("role_id", sa.Integer(), nullable=False),
        sa.Column("permission_id", sa.Integer(), nullable=False),

        sa.ForeignKeyConstraint(
            ["permission_id"],
            ["permissions.id"],
            ondelete="CASCADE",
        ),

        sa.ForeignKeyConstraint(
            ["role_id"],
            ["roles.id"],
            ondelete="CASCADE",
        ),

        sa.PrimaryKeyConstraint(
            "role_id",
            "permission_id",
        ),
    )

    # =========================
    # Add role_id to users
    # =========================

    # Temporarily nullable because existing users
    # already exist in the database.
    op.add_column(
        "users",
        sa.Column(
            "role_id",
            sa.Integer(),
            nullable=True,
        ),
    )

    # =========================
    # Create default employee role
    # =========================

    op.execute(
        """
        INSERT INTO roles (name)
        VALUES ('employee')
        """
    )

    # =========================
    # Assign employee role
    # to existing users
    # =========================

    op.execute(
        """
        UPDATE users
        SET role_id = (
            SELECT id
            FROM roles
            WHERE name = 'employee'
        )
        """
    )

    # =========================
    # Add foreign key
    # =========================

    op.create_foreign_key(
        "fk_users_role_id_roles",
        "users",
        "roles",
        ["role_id"],
        ["id"],
    )

    # =========================
    # Make role_id NOT NULL
    # =========================

    op.alter_column(
        "users",
        "role_id",
        existing_type=sa.Integer(),
        nullable=False,
    )

    # =========================
    # Remove old role column
    # =========================

    op.drop_column(
        "users",
        "role",
    )


def downgrade() -> None:
    """Downgrade schema."""

    # =========================
    # Restore old role column
    # =========================

    op.add_column(
        "users",
        sa.Column(
            "role",
            sa.VARCHAR(length=50),
            nullable=True,
        ),
    )

    # Restore role values from roles table
    op.execute(
        """
        UPDATE users
        SET role = (
            SELECT name
            FROM roles
            WHERE roles.id = users.role_id
        )
        """
    )

    # Make old role column NOT NULL
    op.alter_column(
        "users",
        "role",
        existing_type=sa.VARCHAR(length=50),
        nullable=False,
    )

    # =========================
    # Remove foreign key
    # =========================

    op.drop_constraint(
        "fk_users_role_id_roles",
        "users",
        type_="foreignkey",
    )

    # =========================
    # Remove role_id
    # =========================

    op.drop_column(
        "users",
        "role_id",
    )

    # =========================
    # Remove role_permissions
    # =========================

    op.drop_table(
        "role_permissions",
    )

    # =========================
    # Remove roles
    # =========================

    op.drop_index(
        op.f("ix_roles_name"),
        table_name="roles",
    )

    op.drop_index(
        op.f("ix_roles_id"),
        table_name="roles",
    )

    op.drop_table(
        "roles",
    )

    # =========================
    # Remove permissions
    # =========================

    op.drop_index(
        op.f("ix_permissions_name"),
        table_name="permissions",
    )

    op.drop_index(
        op.f("ix_permissions_id"),
        table_name="permissions",
    )

    op.drop_table(
        "permissions",
    )