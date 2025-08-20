from fastapi import FastAPI
from .controller import UserController



app = FastAPI()
app.include_router(UserController.router)
