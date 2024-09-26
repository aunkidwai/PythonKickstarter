import unittest
import math
from modules.trigonometry import sin, cos, tan, asin, acos, atan, atan2, sinh, cosh, tanh, degrees_to_radians, radians_to_degrees

class TestTrigonometry(unittest.TestCase):
    def test_sin(self):
        self.assertAlmostEqual(sin(30), 0.5, places=7)
        self.assertAlmostEqual(sin(90), 1, places=7)
        self.assertAlmostEqual(sin(0), 0, places=7)
        self.assertAlmostEqual(sin(math.pi/2, use_degrees=False), 1, places=7)

    def test_cos(self):
        self.assertAlmostEqual(cos(60), 0.5, places=7)
        self.assertAlmostEqual(cos(0), 1, places=7)
        self.assertAlmostEqual(cos(90), 0, places=7)
        self.assertAlmostEqual(cos(math.pi, use_degrees=False), -1, places=7)

    def test_tan(self):
        self.assertAlmostEqual(tan(45), 1, places=7)
        self.assertAlmostEqual(tan(0), 0, places=7)
        self.assertAlmostEqual(tan(math.pi/4, use_degrees=False), 1, places=7)

    def test_asin(self):
        self.assertAlmostEqual(asin(0.5), 30, places=7)
        self.assertAlmostEqual(asin(1), 90, places=7)
        self.assertAlmostEqual(asin(0), 0, places=7)
        with self.assertRaises(ValueError):
            asin(2)

    def test_acos(self):
        self.assertAlmostEqual(acos(0.5), 60, places=7)
        self.assertAlmostEqual(acos(1), 0, places=7)
        self.assertAlmostEqual(acos(0), 90, places=7)
        with self.assertRaises(ValueError):
            acos(2)

    def test_atan(self):
        self.assertAlmostEqual(atan(1), 45, places=7)
        self.assertAlmostEqual(atan(0), 0, places=7)

    def test_atan2(self):
        self.assertAlmostEqual(atan2(1, 1), 45, places=7)
        self.assertAlmostEqual(atan2(0, 1), 0, places=7)
        self.assertAlmostEqual(atan2(1, 0), 90, places=7)

    def test_sinh(self):
        self.assertAlmostEqual(sinh(0), 0, places=7)
        self.assertAlmostEqual(sinh(1), 1.1752011936438014, places=7)

    def test_cosh(self):
        self.assertAlmostEqual(cosh(0), 1, places=7)
        self.assertAlmostEqual(cosh(1), 1.5430806348152437, places=7)

    def test_tanh(self):
        self.assertAlmostEqual(tanh(0), 0, places=7)
        self.assertAlmostEqual(tanh(1), 0.7615941559557649, places=7)

    def test_degrees_to_radians(self):
        self.assertAlmostEqual(degrees_to_radians(180), math.pi, places=7)
        self.assertAlmostEqual(degrees_to_radians(90), math.pi/2, places=7)

    def test_radians_to_degrees(self):
        self.assertAlmostEqual(radians_to_degrees(math.pi), 180, places=7)
        self.assertAlmostEqual(radians_to_degrees(math.pi/2), 90, places=7)

if __name__ == '__main__':
    unittest.main()
