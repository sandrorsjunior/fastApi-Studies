from ..auth.Security import Security

from ..config.repository import get_user_repository

from ..repository.UserRepository import UserRepository

from ..config.database import get_db
from ..validations.UserValidation import UserValidation
from ..model.UserModel import UserModel
from ..controller.DTO.UserDTO import ReadUserSchema, CreateUserSchema
from fastapi import Depends, HTTPException

class UserService:
    def __init__(self,
                 user_repository: UserRepository = Depends(get_user_repository),
                 validations: UserValidation = Depends(UserValidation)
                 ):

        self.user_repository = user_repository
        self.validations = validations

    def get_all_users(self) -> list[ReadUserSchema]:
        return self.user_repository.find_all()

    def get_user_by_id(self, user_id: str) -> UserModel | None:
        user = self.user_repository.find_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def save_user(self, user_data: CreateUserSchema) -> UserModel:
        self.validations.duoplicated_name_check(user_data)
        user_data = user_data.model_dump()
        user_data["password"] = Security.encrypt_password(user_data["password"])
        new_user = UserModel(**user_data)
        self.user_repository.save(new_user)
        return new_user

    def update_user(self, user_id: str, user_data: CreateUserSchema) -> UserModel:
        user = self.get_user_by_id(user_id)
        if user:
            user.name = user_data.name
            user.email = user_data.email
            self.user_repository.save(user)
            return user
        else:
            raise HTTPException(status_code=404, detail="User not found")


    def delete_user(self, user_id: str) -> str:
        user = self.get_user_by_id(user_id)
        if user:
            self.user_repository.delete(user)
            return user.id
        else:
            raise HTTPException(status_code=404, detail="User not found")
