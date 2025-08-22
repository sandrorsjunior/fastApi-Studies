from fastapi import UploadFile, File, APIRouter, Depends

from ..service.FileService import FileService


class FileController:
    def __init__(self):
        self.router = APIRouter(
            prefix="/files",
            tags=["files"]
        )
        self.router.add_api_route(
            "/file",
            self.upload_file,
            methods=["POST"],
        )
    
    def upload_file(self, file: UploadFile = File(...), file_service: FileService = Depends(FileService)):
        return file_service.save_file(file)