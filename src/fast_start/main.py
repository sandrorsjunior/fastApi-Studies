from fastapi import FastAPI
from .controller.UserController import UserController
from .config.database import Base, engine  

Base.metadata.create_all(bind=engine)

user_controller = UserController()

app = FastAPI()
app.include_router(user_controller.router)