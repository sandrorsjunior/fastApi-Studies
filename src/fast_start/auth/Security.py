from fastapi import Depends
from sqlalchemy.orm import Session
from ..model.UserModel import UserModel
from ..config.database import get_db
from jwt import encode
from pwdlib import PasswordHash
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import HTTPException, status
from jwt import encode, decode, PyJWTError
from datetime import datetime, timedelta, timezone

SECRET_KEY = 'your-secret-key'  # Isso é provisório, vamos ajustar!
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Security():
    pwd_context = PasswordHash.recommended()
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    @staticmethod
    def encrypt_password(password: str) -> str:
        return Security.pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return Security.pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def check_credentials(db: Session, form_data: OAuth2PasswordRequestForm = Depends()) -> bool:
        user = db.query(UserModel).filter(UserModel.name == form_data.username).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return Security.verify_password(form_data.password, user.password)
    
    @staticmethod
    def create_access_token(data: dict) -> str:
        to_encode = data.copy()
        to_encode.update({"exp": datetime.now(tz=timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)})
        encoded = encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded
    
    @staticmethod
    def check_token(token: str = Depends(oauth2_scheme), 
                    db: Session = Depends(get_db)
                    ) -> UserModel:
        error_unauthorized = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
        try:
            payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            sub = payload.get("sub")
            if sub is None:
                raise error_unauthorized
            user = db.query(UserModel).filter(UserModel.name == sub).first()
            return user
        except PyJWTError:
            raise error_unauthorized
