from fastapi import FastAPI

from .controller.FileController import FileController
from .controller.UserController import UserController
from .config.database import Base, engine  

Base.metadata.create_all(bind=engine)

user_controller = UserController()
file_controller = FileController()
app = FastAPI()
app.include_router(user_controller.router)
app.include_router(file_controller.router)