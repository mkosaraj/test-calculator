import unittest

from calculator import calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator("add", 2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(calculator("add", -2, -3), -5)

    def test_add_floats(self):
        self.assertAlmostEqual(calculator("add", 0.1, 0.2), 0.3)

    def test_subtract(self):
        self.assertEqual(calculator("subtract", 5, 3), 2)

    def test_subtract_negative_result(self):
        self.assertEqual(calculator("subtract", 3, 5), -2)

    def test_multiply(self):
        self.assertEqual(calculator("multiply", 4, 3), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(calculator("multiply", 4, 0), 0)

    def test_multiply_negative(self):
        self.assertEqual(calculator("multiply", -4, 3), -12)

    def test_divide(self):
        self.assertEqual(calculator("divide", 10, 2), 5)

    def test_divide_non_integer_result(self):
        self.assertAlmostEqual(calculator("divide", 7, 2), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator("divide", 5, 0)

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            calculator("modulo", 2, 3)


if __name__ == "__main__":
    unittest.main()
