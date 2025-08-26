import uuid
from pydantic import BaseModel, EmailStr

from .UserFileDTO import UserFileDTO

class CreateUserSchema(BaseModel):
    name: str
    email: EmailStr

class ReadUserSchema(BaseModel):
    id: uuid.UUID
    name: str
    email: EmailStr
    password: str
    files: list[UserFileDTO]

    class Config:
        orm_mode = True  # Allows Pydantic to work with SQLAlchemy objects
