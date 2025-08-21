from sqlalchemy.orm import Session
import uuid

from ..config.database import get_db
from ..validations.UserValidation import UserValidation
from ..model.UserModel import UserModel
from ..controller.DTO.UserDTO import ReadUserSchema, CreateUserSchema
from fastapi import Depends, HTTPException

class UserService:
    def __init__(self, db: Session = Depends(get_db), 
                 validations: UserValidation = Depends(UserValidation)
                 ):
        self.db = db
        self.validations = validations

    def get_all_users(self) -> list[ReadUserSchema]:
        return self.db.query(UserModel).all()

    def get_user_by_id(self, user_id: uuid.UUID) -> UserModel | None:
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()

    def create_user(self, user_data: CreateUserSchema) -> UserModel:
        self.validations.duoplicated_name_check(user_data)
        new_user = UserModel(**user_data.model_dump())
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
