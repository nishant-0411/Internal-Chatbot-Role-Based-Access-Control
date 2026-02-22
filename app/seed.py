import os
import pandas as pd
from app.core.config import engine, SessionLocal, settings
from app.core.security import hash_password
from app.core.logger import logger
from app.models import Base, Employee

def map_department_to_role(department: str):
    department = department.lower()

    mapping = {
        "finance": "finance",
        "marketing": "marketing",
        "hr": "hr",
        "technology": "engineering",
        "data": "engineering",
        "quality assurance": "engineering",
        "product": "engineering",
        "risk": "finance",
        "compliance": "finance",
        "sales": "marketing",
        "operations": "employee",
        "design": "marketing"
    }

    return mapping.get(department, "employee")


logger.info("=" * 60)
logger.info("Starting fresh database setup...")

# Drop and recreate tables
Base.metadata.drop_all(bind=engine)
logger.info("Old tables dropped.")

Base.metadata.create_all(bind=engine)
logger.info("New tables created.")

print("Actual DB Path:", engine.url)
print("CSV Path:", settings.CSV_PATH)
print("Does file exist?:", os.path.exists(settings.CSV_PATH))

db = SessionLocal()

try:
    df = pd.read_csv(settings.CSV_PATH)

    print("Columns:", df.columns)
    print("Total rows in CSV:", len(df))

    created = 0
    skipped = 0

    for _, row in df.iterrows():
        try:
            role = map_department_to_role(row["department"])

            employee = Employee(
                employee_id=row["employee_id"],
                full_name=row["full_name"],
                email=row["email"],
                department=row["department"],
                role=role,
                manager_id=row["manager_id"],
                salary=float(row["salary"]),
                leave_balance=int(row["leave_balance"]),
                leaves_taken=int(row["leaves_taken"]),
                attendance_pct=float(row["attendance_pct"]),
                performance_rating=int(row["performance_rating"]),
                hashed_password=hash_password(settings.DEFAULT_PASSWORD)
            )

            db.add(employee)
            db.commit()
            created += 1

        except Exception as row_error:
            db.rollback()
            skipped += 1
            print(f"⚠️ Skipped row {row['employee_id']} - {row_error}")

    print("✅ Seeding Completed")
    print("Created:", created)
    print("Skipped (duplicates or errors):", skipped)

except Exception as e:
    db.rollback()
    print("🚨 SEEDING FAILED:", e)

finally:
    db.close()
    logger.info("Database session closed.")
    logger.info("=" * 60)