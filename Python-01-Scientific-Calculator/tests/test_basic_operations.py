import unittest
from modules.basic_operations import add, subtract, multiply, divide, modulo, floor_division, negate, absolute

class TestBasicOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-6, 3), -2)
        self.assertAlmostEqual(divide(1, 3), 0.3333333333, places=7)
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_modulo(self):
        self.assertEqual(modulo(7, 3), 1)
        self.assertEqual(modulo(-7, 3), 2)
        with self.assertRaises(ValueError):
            modulo(5, 0)

    def test_floor_division(self):
        self.assertEqual(floor_division(7, 3), 2)
        self.assertEqual(floor_division(-7, 3), -3)
        with self.assertRaises(ValueError):
            floor_division(5, 0)

    def test_negate(self):
        self.assertEqual(negate(5), -5)
        self.assertEqual(negate(-5), 5)
        self.assertEqual(negate(0), 0)

    def test_absolute(self):
        self.assertEqual(absolute(5), 5)
        self.assertEqual(absolute(-5), 5)
        self.assertEqual(absolute(0), 0)

if __name__ == '__main__':
    unittest.main()
