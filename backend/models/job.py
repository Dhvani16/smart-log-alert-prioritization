from sqlalchemy import Column, Integer, String, DateTime
from database.base import Base
from datetime import datetime

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    status = Column(String, default="pending")
    total_logs = Column(Integer, default=0)
    anomaly_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime)