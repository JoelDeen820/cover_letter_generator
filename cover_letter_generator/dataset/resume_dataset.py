import numpy as np
import torch

from torch import Tensor, tensor, from_numpy
from torch.utils.data import Dataset

from cover_letter_generator.dataset.sequence_generator import SequenceGenerator
from cover_letter_generator.dataset.token_converter import TokenConverter


class ResumeDataSet(Dataset):

    def convert_string_to_num_list(self, seq: str):
        return [self.token_converter.get_int_from_token(w) for w in seq.split()]

    def __init__(self, sequence_generator: SequenceGenerator, token_converter: TokenConverter) -> None:
        self.sequence_generator = sequence_generator
        self.token_converter = token_converter
        self.x, self.y = sequence_generator.generate_labeled_data()
        self.int_x = np.array([self.convert_string_to_num_list(seq) for seq in self.x])
        self.int_y = np.array([self.convert_string_to_num_list(seq) for seq in self.y])

    def __len__(self) -> int:
        return len(self.int_x)

    def __getitem__(self, index: int) -> tuple[Tensor, Tensor]:
        return tensor(self.int_x[index], dtype=torch.int32), tensor(self.int_y[index], dtype=torch.int32)