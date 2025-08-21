from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controller.DTO.UserDTO import ReadUserSchema, CreateUserSchema
from ..model.UserModel import UserModel
from ..config.database import get_db
from ..service.UserService import UserService


class UserController:
    def __init__(self):
        self.router = APIRouter(
            prefix="/users",
            tags=["users"]
        )
        self.router.add_api_route("/", 
                                  self.read_users, 
                                  methods=["GET"], 
                                  response_model=list[ReadUserSchema]
                                  )
        self.router.add_api_route("/", 
                                  self.add_new_user, 
                                  methods=["POST"], 
                                  response_model=ReadUserSchema
                                  )

    def read_users(self, user_service: UserService = Depends(UserService)):
        return user_service.get_all_users()

    def add_new_user(self, newUser: CreateUserSchema, user_service: UserService = Depends(UserService)):
        return user_service.create_user(newUser)