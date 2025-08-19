from pydantic import BaseModel, EmailStr

class CreateUserSchema(BaseModel):
    name: str
    email: EmailStr

class ReadUserSchema(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True  # Allows Pydantic to work with SQLAlchemy objects
