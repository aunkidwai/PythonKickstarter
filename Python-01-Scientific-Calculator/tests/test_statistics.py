import unittest
from modules.statistics import mean, median, mode, variance, standard_deviation, range_stat, covariance, correlation

class TestStatistics(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([1, 2, 3, 4, 5]), 3)
        self.assertEqual(mean([-1, 0, 1]), 0)
        with self.assertRaises(ValueError):
            mean([])

    def test_median(self):
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(median([1, 2, 3, 4]), 2.5)
        with self.assertRaises(ValueError):
            median([])

    def test_mode(self):
        self.assertEqual(mode([1, 2, 2, 3, 3, 3, 4]), [3])
        self.assertEqual(set(mode([1, 1, 2, 2])), {1, 2})
        with self.assertRaises(ValueError):
            mode([])

    def test_variance(self):
        self.assertAlmostEqual(variance([1, 2, 3, 4, 5]), 2, places=7)
        with self.assertRaises(ValueError):
            variance([1])

    def test_standard_deviation(self):
        self.assertAlmostEqual(standard_deviation([1, 2, 3, 4, 5]), 1.4142135623730951, places=7)
        with self.assertRaises(ValueError):
            standard_deviation([1])

    def test_range_stat(self):
        self.assertEqual(range_stat([1, 2, 3, 4, 5]), 4)
        self.assertEqual(range_stat([-1, 0, 1]), 2)
        with self.assertRaises(ValueError):
            range_stat([])

    def test_covariance(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 5, 4, 5]
        self.assertAlmostEqual(covariance(x, y), 1.5, places=7)
        with self.assertRaises(ValueError):
            covariance([1], [1])
        with self.assertRaises(ValueError):
            covariance([1, 2], [1])

    def test_correlation(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 5, 4, 5]
        self.assertAlmostEqual(correlation(x, y), 0.7745966692414834, places=7)
        # Add more test cases
        self.assertAlmostEqual(correlation([1, 2, 3], [1, 2, 3]), 1.0, places=7)
        self.assertAlmostEqual(correlation([1, 2, 3], [3, 2, 1]), -1.0, places=7)
        self.assertAlmostEqual(correlation([1, 2, 3], [1, 1, 1]), 0.0, places=7)
        with self.assertRaises(ValueError):
            correlation([1], [1])
        with self.assertRaises(ValueError):
            correlation([1, 2], [1])

if __name__ == '__main__':
    unittest.main()
