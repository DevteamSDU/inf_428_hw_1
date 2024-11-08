import unittest

from code import transform_time_to_cyclic


class TestTimeTransformation(unittest.TestCase):
    def test_midnight(self):
        sin_time, cos_time = transform_time_to_cyclic(0)
        self.assertAlmostEqual(sin_time, 0, places=5)
        self.assertAlmostEqual(cos_time, 1, places=5)

    def test_noon(self):
        sin_time, cos_time = transform_time_to_cyclic(12)
        self.assertAlmostEqual(sin_time, 1, places=5)
        self.assertAlmostEqual(cos_time, 0, places=5)

    def test_evening(self):
        sin_time, cos_time = transform_time_to_cyclic(18)
        self.assertAlmostEqual(sin_time, -math.sqrt(2) / 2, places=5)
        self.assertAlmostEqual(cos_time, -math.sqrt(2) / 2, places=5)

    def test_near_midnight(self):
        sin_time_23, cos_time_23 = transform_time_to_cyclic(23)
        sin_time_1, cos_time_1 = transform_time_to_cyclic(1)

        self.assertAlmostEqual(sin_time_23, sin_time_1, delta=0.2)
        self.assertAlmostEqual(cos_time_23, cos_time_1, delta=0.2)


if __name__ == "__main__":
    unittest.main()
