from app.core.database import SessionLocal
from app.models.role import Role
from app.models.permission import Permission


def seed_rbac():
    db = SessionLocal()

    try:
        # =========================
        # Roles
        # =========================

        role_names = [
            "admin",
            "manager",
            "employee",
        ]

        for role_name in role_names:
            role = (
                db.query(Role)
                .filter(Role.name == role_name)
                .first()
            )

            if not role:
                role = Role(name=role_name)
                db.add(role)

        db.commit()

        # =========================
        # Permissions
        # =========================

        permission_data = [
            ("user:create", "Create users"),
            ("user:read", "View users"),
            ("user:update", "Update users"),
            ("user:delete", "Delete users"),
        ]

        for name, description in permission_data:
            permission = (
                db.query(Permission)
                .filter(Permission.name == name)
                .first()
            )

            if not permission:
                permission = Permission(
                    name=name,
                    description=description,
                )
                db.add(permission)

        db.commit()

        # =========================
        # Get roles
        # =========================

        admin = (
            db.query(Role)
            .filter(Role.name == "admin")
            .first()
        )

        manager = (
            db.query(Role)
            .filter(Role.name == "manager")
            .first()
        )

        employee = (
            db.query(Role)
            .filter(Role.name == "employee")
            .first()
        )

        # =========================
        # Get permissions
        # =========================

        create = (
            db.query(Permission)
            .filter(Permission.name == "user:create")
            .first()
        )

        read = (
            db.query(Permission)
            .filter(Permission.name == "user:read")
            .first()
        )

        update = (
            db.query(Permission)
            .filter(Permission.name == "user:update")
            .first()
        )

        delete = (
            db.query(Permission)
            .filter(Permission.name == "user:delete")
            .first()
        )

        # =========================
        # Assign permissions
        # =========================

        admin.permissions = [
            create,
            read,
            update,
            delete,
        ]

        manager.permissions = [
            read,
            update,
        ]

        employee.permissions = [
            read,
        ]

        db.commit()

        print("RBAC seeded successfully!")

    finally:
        db.close()


if __name__ == "__main__":
    seed_rbac()