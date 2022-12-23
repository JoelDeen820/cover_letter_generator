import unittest
from json import load, dump
from os.path import join, exists, isfile

from cover_letter_generator.dataset.letter_header_db import LetterHeaderDB
from cover_letter_generator.dataset.token_converter import TokenConverter


class TokenConverterTest(unittest.TestCase):
    expected_token_map = {'this': 0, 'is': 1, 'a': 2, 'small': 3, 'dataset': 4, 'for': 5, 'testing': 6, 'randomly': 7,
                          'generated': 8, 'words': 9, 'why': 10, 'being': 11, 'written': 12}
    expected_int_map = ['this', 'is', 'a', 'small', 'dataset', 'for', 'testing', 'randomly', 'generated', 'words',
                        'why', 'being', 'written']

    def setUp(self) -> None:
        test_data = LetterHeaderDB(join('.', 'data', 'small_dataset.txt'))
        self.token_converter = TokenConverter(test_data)

    def test_lines_to_token(self):
        result = list(self.token_converter.int_map)
        self.assertEqual(self.expected_int_map, result)

    def test_token_to_lines(self):
        self.token_converter.create_token_map()
        self.assertEqual(self.expected_token_map, self.token_converter.token_map)

    def test_json_dump(self):
        prefix = join('.', 'data', 'test_token_serialization')
        expected_file_name = prefix + '_token_map.json'
        self.token_converter.dump(join('.', 'data', 'test_token_serialization'))
        self.assertTrue(exists(expected_file_name))
        self.assertTrue(isfile(expected_file_name))
        with open(expected_file_name, 'r') as f:
            result = load(f)
            self.assertEqual(self.expected_token_map, result)

    def test_json_load(self):
        prefix = join('.', 'data', 'test_token_deserialization')
        filepath = prefix + '_token_map.json'
        with open(filepath, 'w') as f:
            dump(self.expected_token_map, f, ensure_ascii=True)
        self.token_converter.load(prefix)
        self.assertEqual(self.expected_token_map, self.token_converter.token_map)


if __name__ == '__main__':
    unittest.main()
