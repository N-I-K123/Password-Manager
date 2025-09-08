from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schema import PasswordsSchema
from models import User
from service import crudPassword
from database import SessionLocal
from auth import get_current_user

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/passwords", tags=["passwords"])

@router.post("/", response_model=PasswordsSchema.PasswordOut)
def create_pass(p: PasswordsSchema.PasswordCreate,
                db: Session = Depends(get_db),
                current_user: str = Depends(get_current_user)):


    user = db.query(User).filter(User.username == current_user).first()
    return crudPassword.create_password(db, p, user.id)

@router.get("/{site}", response_model=PasswordsSchema.PasswordOut)
def read_pass(site: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = db.query(User).filter(User.username == current_user).first()
    passwd = crudPassword.get_password(db, site, user.id)
    if not passwd:
        raise HTTPException(status_code=404, detail="Nie znaleziono hasła")
    return passwd

@router.put("/{site}", response_model=PasswordsSchema.PasswordOut)
def update_pass(
    site: str,
    p: PasswordsSchema.PasswordUpdate,   # tylko nowe hasło
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    user = db.query(User).filter(User.username == current_user).first()
    existing = crudPassword.get_password(db, site, user.id)
    if not existing:
        raise HTTPException(status_code=404, detail="Nie znaleziono hasła")
    return crudPassword.update_password(db, site, p.password, user.id)

@router.delete("/delete/{site}", response_model=PasswordsSchema.PasswordDelete)
def delete_pass(site: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = db.query(User).filter(User.username == current_user).first()
    if not crudPassword.get_password(db, site, user.id):
        raise HTTPException(status_code=404, detail="Brak witryny do usunięcia")
    return crudPassword.delete_password(db, site, user.id)
