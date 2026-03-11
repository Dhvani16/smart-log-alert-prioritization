from sqlalchemy.orm import Session
from models.job import Job

def create_job(db: Session, filename: str):

    job = Job(
        filename=filename,
        status="processing"
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    return job