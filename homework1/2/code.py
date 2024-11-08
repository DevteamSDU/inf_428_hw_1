import numpy as np


def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)


def calculate_aggregated_threat_score(department_data, importance_weights):
    total_weighted_score = 0
    total_importance = sum(importance_weights)

    for threats, weight in zip(department_data, importance_weights):
        department_avg_threat = np.mean(threats)
        total_weighted_score += department_avg_threat * weight

    aggregated_score = (total_weighted_score / total_importance) * (90 / 5)
    return min(90, max(0, aggregated_score))
