from sqlalchemy.orm import Session
from models import Password
from schema.PasswordsSchema import PasswordCreate
from datetime import date
from crypto import encrypt, decrypt
from Generator import generator

key = 'kluczDoSzyfru'
def create_password(db: Session, p: PasswordCreate, user_id: int):
    password_to_store = p.password or generator()

    existing = db.query(Password).filter(
        Password.site == p.site,
        Password.user_id == user_id
    ).first()

    if existing:
        existing.password = decrypt(existing.password, key)
        return existing

    new_pass = Password(
        site=p.site,
        password=encrypt(password_to_store, key),
        created_at=date.today(),
        user_id = user_id
    )

    db.add(new_pass)
    db.commit()
    db.refresh(new_pass)
    new_pass.password = decrypt(new_pass.password, key)
    return new_pass

def get_password(db: Session, site: str, user_id: int):
    passwd_obj = db.query(Password).filter(
        Password.site == site,
        Password.user_id == user_id
    ).first()
    if passwd_obj is None:
        return None
    passwd_obj.password = decrypt(passwd_obj.password, key)
    return passwd_obj


def update_password(db: Session, site: str, new_password: str, user_id: int):
    passwd = db.query(Password).filter(Password.site == site, Password.user_id == user_id).first()
    if new_password == "":
        new_password = generator()
    if passwd:
        passwd.password = encrypt(new_password, key)
        db.commit()
        db.refresh(passwd)
    passwd.password = decrypt(passwd.password, key)
    return passwd

def delete_password(db: Session, site: str,user_id: int):
    passwd = db.query(Password).filter(Password.site == site, Password.user_id == user_id).first()
    if passwd:
        db.delete(passwd)
        db.commit()
    return passwd
