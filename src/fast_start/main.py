from fastapi import FastAPI
from .controller import UserController
from .config.database import Base, engine  

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(UserController.router)
