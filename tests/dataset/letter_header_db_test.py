import unittest
from os.path import join

from cover_letter_generator.dataset.letter_header_db import LetterHeaderDB


class LetterHeaderDBTests(unittest.TestCase):

    def setUp(self) -> None:
        self.data = LetterHeaderDB(join('data', 'test_input_files.txt'))

    def test_inputs(self):
        self.assertEqual('hello world, my name is a random name, and i am interested in your company',
                         self.data.get_header(0))  # add assertion here

    def test_len(self):
        self.assertEqual(4, len(self.data))

if __name__ == '__main__':
    unittest.main()
