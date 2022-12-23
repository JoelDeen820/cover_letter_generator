import unittest
from os.path import join

import torch

from cover_letter_generator.dataset.letter_header_db import LetterHeaderDB
from cover_letter_generator.dataset.resume_dataset import ResumeDataSet
from cover_letter_generator.dataset.sequence_generator import SequenceGenerator
from cover_letter_generator.dataset.token_converter import TokenConverter

test_filepath = join('.', 'data', 'test_sequence_generator.txt')


class DatasetUnitTest(unittest.TestCase):

    def setUp(self) -> None:
        dataset = LetterHeaderDB(test_filepath)
        self.token_converter = TokenConverter(dataset)
        self.sequence_generator = SequenceGenerator(dataset=dataset)
        self.torch_dataset = ResumeDataSet(self.sequence_generator, self.token_converter)

    def test_check_seqence_length(self):
        self.assertEqual(4, len(self.torch_dataset))

    def test_output(self):
        expected_x = torch.tensor([0, 1, 2, 3, 4], dtype=torch.int32)
        expected_y = torch.tensor([1, 2, 3, 4, 5], dtype=torch.int32)
        x, y = self.torch_dataset[0]
        self.assertTrue(torch.equal(expected_x, x))
        self.assertTrue(torch.equal(expected_y, y))


if __name__ == '__main__':
    unittest.main()
