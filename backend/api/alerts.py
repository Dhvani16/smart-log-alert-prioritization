from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import SessionLocal
from models.alert import Alert

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/alerts/{job_id}")
def get_alerts(job_id: int, limit: int = 50, db: Session = Depends(get_db)):

    alerts = (
        db.query(Alert)
        .filter(Alert.job_id == job_id)
        .order_by(Alert.severity_score.desc())
        .limit(limit)
        .all()
    )

    return [
        {
            "log_level": a.log_level,
            "anomaly_score": a.anomaly_score,
            "severity_score": a.severity_score,
            "severity_level": a.severity_level
        }
        for a in alerts
    ]