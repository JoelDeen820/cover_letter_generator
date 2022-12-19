import unittest
from os.path import join
import numpy as np

from cover_letter_generator.dataset.letter_header_db import LetterHeaderDB
from cover_letter_generator.dataset.token_converter import TokenConverter


class TokenConverterTest(unittest.TestCase):

    def setUp(self) -> None:
        test_data = LetterHeaderDB(join('.', 'data', 'empty_file.txt'))
        self.token_converter = TokenConverter(test_data)

    def test_lines_to_token(self):
        expected_result = ['this', 'is', 'a', 'small', 'dataset', 'for', 'testing', 'randomly', 'generated', 'words',
                           'why', 'being', 'written']
        test_data = LetterHeaderDB(join('.', 'data', 'small_dataset.txt'))
        self.token_converter.create_int_map(test_data)
        result = list(self.token_converter.int_map)
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
