from sqlalchemy import Column, Integer, String, Float, DateTime
from database.base import Base

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer)
    timestamp = Column(DateTime)
    log_level = Column(String)
    message = Column(String)

    anomaly_score = Column(Float)
    severity_score = Column(Float)
    severity_level = Column(String)