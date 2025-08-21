from fastapi.params import Depends

from ..config.database import get_db
from ..controller.DTO.UserDTO import CreateUserSchema
from ..model.UserModel import UserModel
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

class UserValidation:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
    def duoplicated_name_check(self, user_data: CreateUserSchema):
        user_iqual_name = self.db.query(UserModel).filter(UserModel.name == user_data.name).first()
        
        if user_iqual_name:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Name already registered"
            )