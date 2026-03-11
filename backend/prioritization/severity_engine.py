import math

def compute_severity(log_level, anomaly_score, frequency):

    level_weights = {
        "INFO": 0.1,
        "WARN": 0.4,
        "ERROR": 0.7,
        "FATAL": 1.0
    }

    log_weight = level_weights.get(log_level, 0.1)

    anomaly_component = abs(anomaly_score)

    freq_score = min(math.log1p(frequency) / 5, 1.0)

    burst_score = freq_score

    severity_score = (
        0.4 * log_weight +
        0.3 * anomaly_component +
        0.2 * freq_score +
        0.1 * burst_score
    )

    return severity_score

def classify_severity(score):

    if score >= 0.75:
        return "critical"

    elif score >= 0.4:
        return "medium"

    else:
        return "low"