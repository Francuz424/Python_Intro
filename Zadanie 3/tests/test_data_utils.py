import unittest
from my_awesome_lib import data_utils

class TestDataUtils(unittest.TestCase):
    def test_normalize_list(self):
        result = data_utils.normalize_list([0, 50, 100])
        self.assertAlmostEqual(result[1], 0.5)

    def test_flatten(self):
        self.assertEqual(data_utils.flatten([[1, 2], [3]]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()