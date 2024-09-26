import unittest
import math
from modules.advanced_operations import power, square_root, factorial, logarithm, natural_logarithm, exponential, absolute_value, floor, ceiling

class TestAdvancedOperations(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(power(5, 1), 5)
        self.assertAlmostEqual(power(2, 0.5), math.sqrt(2), places=7)

    def test_square_root(self):
        self.assertEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(2), math.sqrt(2), places=7)
        with self.assertRaises(ValueError):
            square_root(-1)

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(3.5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(100, 10), 2, places=7)
        self.assertAlmostEqual(logarithm(8, 2), 3, places=7)
        with self.assertRaises(ValueError):
            logarithm(0, 10)
        with self.assertRaises(ValueError):
            logarithm(10, 0)
        with self.assertRaises(ValueError):
            logarithm(10, 1)

    def test_natural_logarithm(self):
        self.assertAlmostEqual(natural_logarithm(math.e), 1, places=7)
        self.assertAlmostEqual(natural_logarithm(1), 0, places=7)
        with self.assertRaises(ValueError):
            natural_logarithm(0)
        with self.assertRaises(ValueError):
            natural_logarithm(-1)

    def test_exponential(self):
        self.assertAlmostEqual(exponential(0), 1, places=7)
        self.assertAlmostEqual(exponential(1), math.e, places=7)
        self.assertAlmostEqual(exponential(-1), 1/math.e, places=7)

    def test_absolute_value(self):
        self.assertEqual(absolute_value(5), 5)
        self.assertEqual(absolute_value(-5), 5)
        self.assertEqual(absolute_value(0), 0)

    def test_floor(self):
        self.assertEqual(floor(3.7), 3)
        self.assertEqual(floor(-3.7), -4)
        self.assertEqual(floor(0), 0)

    def test_ceiling(self):
        self.assertEqual(ceiling(3.7), 4)
        self.assertEqual(ceiling(-3.7), -3)
        self.assertEqual(ceiling(0), 0)

if __name__ == '__main__':
    unittest.main()
