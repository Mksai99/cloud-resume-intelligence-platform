from fastapi import APIRouter, UploadFile, File
from app.services.s3_service import upload_file_to_s3

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    file_url = upload_file_to_s3(file.file, file.filename)

    return {
        "filename": file.filename,
        "file_url": file_url,
        "message": "Resume uploaded successfully to S3"
    }