import unittest

from cover_letter_generator.dataset.dataset import ResumeDataSet


class DatasetUnitTest(unittest.TestCase):

    def setUp(self) -> None:
        test_data = ["Hello World, my name is a random name, and I am interested in your company",
                     "This is a small dataset for testing randomly generated words, why is this being writen",
                     "I have experience writing chickens that may help your chickens lead chicken kind",
                     "Neural Networks are great little things that help solve some of the problems"
                     ]
        self.dataset = ResumeDataSet(5, test_data, "Hello, I have a name, and I am interested in your company")

    def test_check_seqence_length(self):
        result = self.dataset.sequence_length
        self.assertEqual(5, result)
