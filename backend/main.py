from fastapi import FastAPI
from api import logs
from database.db import engine
from database.base import Base

from models import job, alert

app = FastAPI()
app.include_router(logs.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"system": "Smart Log Alert Prioritization"}