from typing import Generic, Type, TypeVar
from fastapi import Depends
from ..config.database import get_db
from sqlalchemy.orm import Session
from ..controller.DTO.UserDTO import CreateUserSchema

ID = TypeVar('ID')
T = TypeVar('T')
class BaseRepository(Generic[T, ID]):
    def __init__(self, model:Type[T], db: Session):
        self.db = db
        self.model = model

    def save(self,user: T):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def find_by_id(self, id:ID) -> T | None:
        return self.db.query(self.model).filter(self.model.id == id).first()

    def find_all(self) -> list[T]:
        return self.db.query(self.model).all()

    def delete(self, user: T) -> ID:
        self.db.delete(user)
        self.db.commit()
        return user.id

