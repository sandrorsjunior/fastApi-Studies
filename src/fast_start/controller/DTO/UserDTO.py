import uuid
from pydantic import BaseModel, EmailStr

from .UserFileDTO import UserFileDTO

class CreateUserSchema(BaseModel):
    name: str
    email: EmailStr
    files: list[UserFileDTO]

class ReadUserSchema(BaseModel):
    id: uuid.UUID
    name: str
    email: EmailStr

    class Config:
        orm_mode = True  # Allows Pydantic to work with SQLAlchemy objects
