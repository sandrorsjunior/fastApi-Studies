from typing import Generic, TypeVar
from fastapi import Depends
from ..config.database import get_db
from sqlalchemy.orm import Session
from ..model.UserModel import UserModel
from ..controller.DTO.UserDTO import CreateUserSchema

elementData = TypeVar('elementData')
class UserRepository(Generic[elementData]):
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def save(self,user: elementData):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

