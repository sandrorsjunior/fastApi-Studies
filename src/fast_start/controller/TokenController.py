from fastapi import Depends, APIRouter, HTTPException, status
from .DTO.tokenDTO import TokenResponse
from ..config.database import get_db
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from ..auth.Security import Security

class TokenController():
    
    def __init__(self):

        self.router = APIRouter(prefix="/token", 
                       tags=["Token"]
                       )
        
        self.router.add_api_route("/", 
                                  self.generate_token, 
                                  methods=["POST"], 
                                  response_model=TokenResponse
                                  )

    def generate_token(self, form_data: OAuth2PasswordRequestForm = Depends(),
                       db: Session = Depends(get_db)
                       ):
        if not Security.check_credentials(db, form_data):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token = Security.create_access_token(
            data={"sub": form_data.username}
        )
        return TokenResponse(access_token=access_token, token_type="bearer")
    
    