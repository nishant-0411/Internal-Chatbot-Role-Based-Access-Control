from models import Base, User
from app.core.config import engine, SessionLocal
from app.core.security import hash_password

Base.metadata.create_all(bind = engine)

db = SessionLocal()

users = [
    {"username": "Jatin", "password": "1234", "role": "finance"},
    {"username": "Yash", "password": "1234", "role": "marketing"},
    {"username": "Kapil", "password": "1234", "role": "engineering"},
    {"username": "Nishant", "password": "1234", "role": "c-level"},
]

for user in users:
    existing = db.query(User).filter(User.username == user["username"]).first()

    if not existing:
        db_user = User(
            username = user["username"],
            hashed_password = hash_password(user["password"]),
            role = user["role"]
        )
        db.add(db_user)

db.commit()
db.close()

print("Users seeded successfully!")

