from .BaseRepository import BaseRepository
from ..model.UserFileModel import UserFileModel
from fastapi import Depends
from sqlalchemy.orm import Session
from ..config.database import get_db


class UserMetaDataFileRepository(BaseRepository[UserFileModel, str]):
    def __ini__(self, db: Session = Depends(get_db)):
        super().__init__(UserFileModel, db)