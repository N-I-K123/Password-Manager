from fastapi import FastAPI
import models
from database import engine
from controller import passwords, users

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(passwords.router)
app.include_router(users.router)
