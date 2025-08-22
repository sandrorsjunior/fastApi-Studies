from sqlalchemy import ForeignKey, String
from ..config.database import Base
from sqlalchemy.orm import Mapped, mapped_column, Relationship
import uuid

from ..model.UserModel import UserModel

class UserFileModel(Base):
    __tablename__ = 'user_files'
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    file_path: Mapped[str] = mapped_column(String, nullable=False, unique=False)
    file_type: Mapped[str] = mapped_column(String, nullable=False, unique=False)
    file_name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    user: Mapped[UserModel] = Relationship(back_populates="files")
