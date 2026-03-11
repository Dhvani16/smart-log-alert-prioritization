from sklearn.ensemble import IsolationForest

def detect_anomalies(features):

    model = IsolationForest(
        n_estimators=100,
        contamination=0.05,
        random_state=42
    )

    model.fit(features)

    anomaly_scores = model.decision_function(features)

    predictions = model.predict(features)

    return anomaly_scores, predictions