from ..repository.UserRepository import UserRepository
from ..repository.UserMetaDataFileRepository import UserMetaDataFileRepository
from fastapi import Depends
from sqlalchemy.orm import Session
from ..config.database import get_db

def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db)

def get_user_meta_data_repository(db: Session = Depends(get_db)) -> UserMetaDataFileRepository:
    return UserMetaDataFileRepository(db)