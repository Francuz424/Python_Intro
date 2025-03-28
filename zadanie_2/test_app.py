import unittest
from app import (
    is_valid_email,
    calculate_rectangle_area,
    filter_and_sort_numbers,
    convert_date_format,
    is_palindrome,
)

class TestApp(unittest.TestCase):

    def test_is_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertFalse(is_valid_email("invalid-email"))
        self.assertFalse(is_valid_email("user@.com"))

    def test_calculate_rectangle_area(self):
        self.assertEqual(calculate_rectangle_area(5, 10), 50)
        self.assertEqual(calculate_rectangle_area(0, 0), 0)
        with self.assertRaises(ValueError):
            calculate_rectangle_area(-3, 5)

    def test_filter_and_sort_numbers(self):
        self.assertEqual(filter_and_sort_numbers([3, -1, 2, 0]), [0, 2, 3])
        self.assertEqual(filter_and_sort_numbers([]), [])
        self.assertEqual(filter_and_sort_numbers([-5, -2]), [])

    def test_convert_date_format(self):
        self.assertEqual(convert_date_format("28-03-2025"), "2025/03/28")
        with self.assertRaises(ValueError):
            convert_date_format("2025-03-28")
        with self.assertRaises(ValueError):
            convert_date_format("31-02-2023")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("Kajak"))
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome("Hello"))

if __name__ == '__main__':
    unittest.main()