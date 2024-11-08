import unittest

from code import calculate_aggregated_threat_score, generate_random_data


class TestAggregatedThreatScore(unittest.TestCase):
    def test_equal_importance_equal_threats(self):
        departments = [generate_random_data(30, 5, 50) for _ in range(5)]
        importance = [3, 3, 3, 3, 3]
        score = calculate_aggregated_threat_score(departments, importance)
        self.assertTrue(0 <= score <= 90)

    def test_different_importance_different_threats(self):
        departments = [
            generate_random_data(20, 5, 40),
            generate_random_data(40, 10, 50),
            generate_random_data(60, 15, 70),
            generate_random_data(30, 5, 20),
            generate_random_data(10, 3, 100)
        ]
        importance = [5, 3, 4, 2, 1]
        score = calculate_aggregated_threat_score(departments, importance)
        self.assertTrue(0 <= score <= 90)

    def test_all_high_threat_high_importance(self):
        departments = [generate_random_data(80, 5, 50) for _ in range(5)]
        importance = [5, 5, 5, 5, 5]
        score = calculate_aggregated_threat_score(departments, importance)
        self.assertTrue(score > 70)

    def test_all_low_threat_low_importance(self):
        departments = [generate_random_data(5, 3, 50) for _ in range(5)]
        importance = [1, 1, 1, 1, 1]
        score = calculate_aggregated_threat_score(departments, importance)
        self.assertTrue(score < 20)

    def test_single_department(self):
        departments = [generate_random_data(40, 10, 100)]
        importance = [3]
        score = calculate_aggregated_threat_score(departments, importance)
        self.assertTrue(0 <= score <= 90)


if __name__ == "__main__":
    unittest.main()
