import pandas as pd
import re
from anomaly_detection.isolation_forest import detect_anomalies
from models.alert import Alert
from models.job import Job
from sqlalchemy.orm import Session

def parse_logs(file_path):

    logs = []

    with open(file_path, "r") as f:
        for line in f:

            parts = line.strip().split()

            if len(parts) < 5:
                continue

            log_level = parts[3]
            message = " ".join(parts[4:])

            logs.append({
                "log_level": log_level,
                "message": message,
                "message_length": len(message)
            })

    df = pd.DataFrame(logs)

    return df

def extract_features(df):

    level_map = {
        "INFO": 1,
        "WARN": 2,
        "ERROR": 3,
        "FATAL": 4
    }

    df["log_level_num"] = df["log_level"].map(level_map).fillna(0)

    df["frequency"] = df.groupby("message")["message"].transform("count")

    features = df[[
        "log_level_num",
        "message_length",
        "frequency"
    ]]

    return df, features

def store_alerts(df, scores, preds, job_id, db: Session):

    for i in range(len(df)):

        if preds[i] == -1:

            alert = Alert(
                job_id=job_id,
                log_level=df.iloc[i]["log_level"],
                message=df.iloc[i]["message"],
                anomaly_score=float(scores[i]),
                severity_score=0,
                severity_level="low"
            )

            db.add(alert)

    db.commit()

def process_logs(file_path, job_id, db):

    # df = parse_logs(file_path)

    # df, features = extract_features(df)

    # scores, preds = detect_anomalies(features)

    # store_alerts(df, scores, preds, job_id, db)

    print("Parsing logs...")
    df = parse_logs(file_path)

    print("Extracting features...")
    df, features = extract_features(df)

    print("Detecting anomalies...")
    scores, preds = detect_anomalies(features)

    print("Storing alerts...")
    store_alerts(df, scores, preds, job_id, db)

    print("Done")

    # --- Job statistics ---
    total_logs = int(len(df))
    anomaly_count = int((preds == -1).sum())

    job = db.query(Job).filter(Job.id == job_id).first()

    job.total_logs = total_logs
    job.anomaly_count = anomaly_count
    job.status = "completed"

    db.commit()

    return total_logs