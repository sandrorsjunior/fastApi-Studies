from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from ..config.database import Base
import uuid


class UserModel(Base):
    __tablename__ = 'users'
    id: Mapped[str] = mapped_column(
        String(36), 
        primary_key=True, 
        default=lambda: str(uuid.uuid4())
        )
    name:Mapped[str] = mapped_column(nullable=False, unique=False)
    email:Mapped[str] = mapped_column(nullable=False, unique=False)