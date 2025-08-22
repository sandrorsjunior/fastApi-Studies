from sqlalchemy.orm import Session
import uuid

from ..model.UserFileModel import UserFileModel

from ..controller.DTO.UserFileDTO import UserFileDTO
from ..config.repository import get_user_meta_data_repository
from ..repository.UserMetaDataFileRepository import UserMetaDataFileRepository
from ..config.database import get_db
from fastapi import Depends, HTTPException, UploadFile, File

class FileService:
    def __init__(self, 
                 db: Session = Depends(get_db), 
                 userMetaDataRepository: UserMetaDataFileRepository = Depends(get_user_meta_data_repository)
                 ):
        self.db = db
        self.userMetaDataRepository = userMetaDataRepository

    def save_file(self, file_metadata: UploadFile, user_id: str) -> UserFileModel:
        file_model = UserFileModel(
            file_name=file_metadata.filename,
            file_path=f"./uploads/{file_metadata.filename}",
            file_type=file_metadata.content_type,
            user_id=user_id
        )
        try:
            with open(file_model.file_path, "wb") as buffer:
                buffer.write(file_metadata.file.read())
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to save file: {str(e)}")

        self.userMetaDataRepository.save(file_model)
        return file_model

    def get_all_user_files(self) -> list[UserFileModel]:
        return self.userMetaDataRepository.find_all()
