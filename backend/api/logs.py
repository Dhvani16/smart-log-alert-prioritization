from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
import shutil
import os

from database.db import SessionLocal
from services.job_service import create_job
from services.log_service import process_logs

router = APIRouter()

UPLOAD_DIR = "uploaded_logs"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/logs/upload")
async def upload_logs(file: UploadFile = File(...), db: Session = Depends(get_db)):

    # Ensure directory exists
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_location = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    job = create_job(db, file.filename)

    process_logs(file_location, job.id, db)

    return {
        "job_id": job.id,
        "filename": file.filename,
        "status": job.status
    }