from fastapi import FastAPI, Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from schema import UserSchema
from auth import create_access_token, verify_password
from datetime import timedelta
from service import crudUser

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.post("/register")
def register(user: UserSchema.UserCreate, db: Session = Depends(get_db)):

    return crudUser.create_user(db, user)

@router.post("/token")
def login(user: UserSchema.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Bad credentials")
    access_token_expires = timedelta(minutes=30)
    token = create_access_token({"sub": db_user.username}, access_token_expires)
    return {"access_token": token, "token_type": "bearer"}


@router.get("/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    from jose import jwt, JWTError
    from auth import SECRET_KEY, ALGORITHM

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    return {"username": username}
