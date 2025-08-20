from sqlalchemy.orm import Mapped, mapped_column
from ..config.database import Base
import uuid


class UserModel(Base):
    __tablename__ = 'users'
    id:Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    email:Mapped[str] = mapped_column(nullable=False, unique=True)