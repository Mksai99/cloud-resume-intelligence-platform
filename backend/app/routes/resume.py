from fastapi import APIRouter, UploadFile, File
from app.services.s3_service import upload_file_to_s3
from app.services.resume_parser import (
    extract_text_from_pdf,
    clean_resume_text
)
from app.services.comprehend_service import detect_entities
from app.utils.skill_extractor import extract_skills

import shutil

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

UPLOAD_DIR = "uploads"

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    local_file_path = f"{UPLOAD_DIR}/{file.filename}"

    # Save locally
    with open(local_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    extracted_text = extract_text_from_pdf(local_file_path)

    # Clean text
    cleaned_text = clean_resume_text(extracted_text)

    # Detect AWS entities
    entities = detect_entities(extracted_text)

    # Extract technical skills
    skills = extract_skills(cleaned_text)

    # Upload to S3
    with open(local_file_path, "rb") as uploaded_file:
        file_url = upload_file_to_s3(
            uploaded_file,
            file.filename
        )

    return {
        "filename": file.filename,
        "file_url": file_url,
        "skills_detected": skills,
        "entities_detected": entities[:10],
        "message": "Resume analyzed successfully"
    }