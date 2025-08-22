from fastapi.params import Depends

from ..config.database import get_db
from ..model.UserModel import UserModel
from ..repository.BaseRepository import BaseRepository
from sqlalchemy.orm import Session

class UserRepository(BaseRepository[UserModel, str]):
    def __init__(self, db: Session):
        super().__init__(UserModel,db)
