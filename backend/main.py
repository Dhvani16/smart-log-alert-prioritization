from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import logs, alerts
from database.db import engine
from database.base import Base

from models import job, alert

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(logs.router)
app.include_router(alerts.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"system": "Smart Log Alert Prioritization"}