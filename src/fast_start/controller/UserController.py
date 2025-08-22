import uuid
from fastapi import APIRouter, Depends, UploadFile
from fastapi.params import File
from sqlalchemy.orm import Session

from ..service.FileService import FileService
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
        self.router.add_api_route("/{user_id}", 
                                  self.get_user_by_id, 
                                  methods=["GET"], 
                                  response_model=ReadUserSchema
                                  )
        self.router.add_api_route("/", 
                                  self.add_new_user, 
                                  methods=["POST"], 
                                  response_model=ReadUserSchema
                                  )
        self.router.add_api_route("/{user_id}", 
                                  self.update_user, 
                                  methods=["PUT"], 
                                  response_model=ReadUserSchema
                                  )
        self.router.add_api_route("/{user_id}", 
                                  self.delete_user, 
                                  methods=["DELETE"], 
                                  response_model=str
                                  )

    def read_users(self, user_service: UserService = Depends(UserService)):
        return user_service.get_all_users()
    
    def get_user_by_id(self, user_id: str, user_service: UserService = Depends(UserService)):
        return user_service.get_user_by_id(user_id)

    def add_new_user(self, 
                     newUser: CreateUserSchema, 
                     user_service: UserService = Depends(UserService)
                     ):
        return user_service.save_user(newUser)
    
    def update_user(self, user_id: str, updated_data: CreateUserSchema, user_service: UserService = Depends(UserService)):
        return user_service.update_user(user_id, updated_data) 
    
    def delete_user(self, user_id: str, user_service: UserService = Depends(UserService)):
        return user_service.delete_user(user_id)