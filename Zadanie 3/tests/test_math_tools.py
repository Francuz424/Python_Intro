import unittest
from my_awesome_lib import math_tools

class TestMathTools(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(math_tools.is_prime(7))
        self.assertFalse(math_tools.is_prime(8))

    def test_factorial(self):
        self.assertEqual(math_tools.factorial(5), 120)
        self.assertRaises(ValueError, math_tools.factorial, -1)

if __name__ == '__main__':
    unittest.main()