from fastapi import UploadFile, File, APIRouter, Depends

from ..service.FileService import FileService
from .DTO.UserFileDTO import UserFileDTO

class FileController:
    def __init__(self):
        self.router = APIRouter(
            prefix="/files",
            tags=["files"]
        )
        self.router.add_api_route(
            "/{user_id}",
            self.upload_file,
            methods=["POST"],
        )
        self.router.add_api_route(
            "/",
            self.get_all_files,
            methods=["GET"],
            response_model=list[UserFileDTO]
        )

    def upload_file(self, user_id: str, file: UploadFile = File(...), file_service: FileService = Depends(FileService)):
        return file_service.save_file(file, user_id)
    
    def get_all_files(self, file_service: FileService = Depends(FileService)):
        return file_service.get_all_user_files()