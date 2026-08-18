import unittest
from give_bmi import give_bmi, apply_limit

class TestGiveBMI(unittest.TestCase):

    def test_normal_values(self):
        h = [1.80, 1.65, 1.50]
        w = [80, 62, 45]
        result = give_bmi(h, w)
        self.assertEqual(len(result), 3)
        self.assertAlmostEqual(result[0], 80 / (1.80**2))

    def test_float_values(self):
        h = [2.71, 1.15]
        w = [165.3, 38.4]
        result = give_bmi(h, w)
        self.assertAlmostEqual(result[0], 165.3 / (2.71**2))
        self.assertAlmostEqual(result[1], 38.4 / (1.15**2))

    def test_size_mismatch(self):
        h = [1.70, 1.80]
        w = [70]
        with self.assertRaises(Exception):
            give_bmi(h, w)

    def test_invalid_type(self):
        h = [1.70, "abc", 1.60]
        w = [70, 80, 60]
        with self.assertRaises(Exception):
            give_bmi(h, w)


class TestApplyLimit(unittest.TestCase):

    def test_normal_limit(self):
        bmi = [22.5, 29.0, 31.2]
        result = apply_limit(bmi, 26)
        self.assertEqual(result, [False, True, True])

    def test_high_limit(self):
        bmi = [10, 15, 20]
        result = apply_limit(bmi, 50)
        self.assertEqual(result, [False, False, False])

    def test_invalid_type(self):
        bmi = [22.5, "xyz", 30]
        with self.assertRaises(Exception):
            apply_limit(bmi, 25)

    def test_invalid_limit_type(self):
        bmi = [22.5, 30.1]
        with self.assertRaises(Exception):
            apply_limit(bmi, "vinte")


if __name__ == "__main__":
    unittest.main()
