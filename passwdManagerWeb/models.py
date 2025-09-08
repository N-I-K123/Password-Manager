from sqlalchemy import Column, Integer, String, Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Password(Base):
    __tablename__ = "passwords"
    id = Column(Integer, primary_key=True)
    site = Column(String)
    password = Column(String)
    created_at = Column(Date)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="passwords")

    __table_args__ = (
        UniqueConstraint('user_id', 'site', name='uix_user_site'),
    )

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    passwords = relationship("Password", back_populates="owner")
