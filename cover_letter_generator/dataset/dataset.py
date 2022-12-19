from re import sub

from torch import Tensor, tensor
from torch.utils.data import Dataset

clas

class ResumeDataSet(Dataset):

    def remove_punctuation(self):
        [sub("[^a-z' ]", "", i).lower() for i in self.word_sequences]

    def __init__(self, sequence_len: int, dataset: list[str], intro_sentence: str) -> None:
        self.sequence_length = sequence_len
        self.word_sequences = dataset
        self.intro_sentence = intro_sentence
        self.remove_punctuation()

    def __len__(self) -> int:
        return len(self.word_dataset)

    def __getitem__(self, index) -> Tensor:
        return tensor([1])
