from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import (
    sessionLocal,
    User
)
from .schema import CreateUserSchema, ReadUserSchema


app = FastAPI()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/users')
def read_users(db: Session = Depends(get_db)) -> list[ReadUserSchema]:
    users = db.query(User).all()
    return users

@app.post('/users', response_model=ReadUserSchema)
def add_new_user(newUser: CreateUserSchema, db: Session = Depends(get_db)):
    db_user = User(**newUser.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user