from ..repository.UserRepository import UserRepository
from fastapi import Depends
from sqlalchemy.orm import Session
from ..config.database import get_db

def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db)