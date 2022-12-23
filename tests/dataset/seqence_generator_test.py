import unittest
from os.path import join

from cover_letter_generator.dataset.letter_header_db import LetterHeaderDB
from cover_letter_generator.dataset.sequence_generator import SequenceGenerator

test_filepath = join('.', 'data', 'test_sequence_generator.txt')


class SequenceGeneratorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.dataset = LetterHeaderDB(test_filepath)

    def test_dataset_setup(self):
        expected_dataset = ['this is a small dataset for', 'is a small dataset for testing',
                            'i have experience writing chickens',
                            'that sounds about right']
        generator = SequenceGenerator(dataset=self.dataset)
        expected_gen = SequenceGenerator(input_sequences=expected_dataset)
        self.assertEqual(expected_gen, generator)

    def test_equality(self):
        base_seq = SequenceGenerator(input_sequences=['Hello', 'World'])
        self.assertNotEquals(base_seq, ['Hello', 'World'])
        self.assertNotEquals(base_seq, None)
        self.assertNotEquals(base_seq, SequenceGenerator(input_sequences=['Hello']))
        self.assertEquals(base_seq, SequenceGenerator(input_sequences=['Hello', 'World']))

    def test_labeled_data(self):
        expected_x = ['this is a small dataset', 'is a small dataset for', 'i have experience writing',
                      'that sounds about']
        expected_y = ['is a small dataset for', 'a small dataset for testing', 'have experience writing chickens',
                      'sounds about right']
        generator = SequenceGenerator(dataset=self.dataset)
        x, y = generator.generate_labeled_data()
        self.assertEqual(expected_x, x)
        self.assertEqual(expected_y, y)


if __name__ == '__main__':
    unittest.main()
