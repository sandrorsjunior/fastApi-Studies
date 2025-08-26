from fastapi import FastAPI

from .controller.FileController import FileController
from .controller.UserController import UserController
from .controller.TokenController import TokenController
from .config.database import Base, engine  

Base.metadata.create_all(bind=engine)

user_controller = UserController()
file_controller = FileController()
token_controller = TokenController()

app = FastAPI()
app.include_router(user_controller.router)
app.include_router(file_controller.router)
app.include_router(token_controller.router)