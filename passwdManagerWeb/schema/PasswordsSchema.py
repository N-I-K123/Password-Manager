from pydantic import BaseModel
from datetime import date

class PasswordBase(BaseModel):
    site: str
    password: str

class PasswordCreate(PasswordBase):
    pass
class PasswordUpdate(BaseModel):
    password: str

class PasswordOut(PasswordBase):
    site: str
    password: str
    created_at: date

    model_config = {
        "from_attributes": True
    }

class PasswordDelete(PasswordBase):
    pass
