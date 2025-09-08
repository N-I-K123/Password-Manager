from sqlalchemy.orm import Session
import models
from auth import get_password_hash
from schema.UserSchema import UserCreate

def create_user(db: Session, user: UserCreate):
    hashed_pw = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)


    return {"msg": "User created"}