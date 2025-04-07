import unittest
from my_awesome_lib import text_processing

class TestTextProcessing(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(text_processing.count_words("Hello world"), 2)

    def test_remove_punctuation(self):
        self.assertEqual(text_processing.remove_punctuation("Hello, world!"), "Hello world")

if __name__ == '__main__':
    unittest.main()