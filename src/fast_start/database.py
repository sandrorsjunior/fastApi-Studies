from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]

engine = create_engine('sqlite:///fast_start.db')

# This line tells SQLAlchemy to create all database tables defined by your models (like User)
# in the database specified by 'engine' (here, 'sqlite:///fast_start.db').
# It checks your model classes and creates the corresponding tables if they don't already exist.
Base.metadata.create_all(bind=engine)


sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)