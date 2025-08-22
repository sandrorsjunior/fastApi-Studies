from pydantic import BaseModel

class UserFileDTO(BaseModel):
    id: str
    file_name: str
    file_path: str
    file_type: str
    
    class Config:
        orm_mode = True  # Allows Pydantic to work with SQLAlchemy objects