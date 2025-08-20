from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controller.DTO.UserDTO import ReadUserSchema, CreateUserSchema
from ..model.UserModel import UserModel
from ..config.database import get_db

router = APIRouter(
    prefix="/users",  # All routes will start with /users
    tags=["users"]    # Grouping for docs
)

@router.get('/')
def read_users(db: Session = Depends(get_db)) -> list[ReadUserSchema]:
    users = db.query(UserModel).all()
    return users

@router.post('/', response_model=ReadUserSchema)
def add_new_user(newUser: CreateUserSchema, db: Session = Depends(get_db)):
    db_user = UserModel(**newUser.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user