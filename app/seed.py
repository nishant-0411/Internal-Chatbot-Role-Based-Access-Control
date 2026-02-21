from models import Base, User
from app.core.config import engine, SessionLocal
from app.core.security import hash_password
from app.core.logger import logger

logger.info("Starting database seeding process...")

Base.metadata.create_all(bind = engine)
logger.info("Database tables ensured.")

db = SessionLocal()

users = [
    {"username": "Jatin", "password": "1234", "role": "finance"},
    {"username": "Yash", "password": "1234", "role": "marketing"},
    {"username": "Kapil", "password": "1234", "role": "engineering"},
    {"username": "Nishant", "password": "1234", "role": "c-level"},
]

created_count = 0
skipped_count = 0

try:
    for user in users:
        existing = db.query(User).filter(User.username == user["username"]).first()

        if not existing:
            db_user = User(
                username=user["username"],
                hashed_password=hash_password(user["password"]),
                role=user["role"]
            )
            db.add(db_user)
            created_count += 1
            logger.info(f"User created: {user['username']} | Role: {user['role']}")
        else:
            skipped_count += 1
            logger.warning(f"User already exists, skipped: {user['username']}")

    db.commit()
    logger.info("Database commit successful.")

except Exception as e:
    db.rollback()
    logger.error(f"Error during seeding: {str(e)}")

finally:
    db.close()
    logger.info("Database session closed.")

logger.info(f"Seeding completed. Created: {created_count}, Skipped: {skipped_count}")
logger.info("-" * 60)

