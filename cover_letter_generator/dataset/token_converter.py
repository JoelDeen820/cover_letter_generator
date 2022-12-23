from json import dump

import numpy as np

from cover_letter_generator.dataset.letter_header_db import LetterHeaderDB


class TokenConverter(object):

    def parse_line(self, line : str) -> None:
        for word in line.split():
            if word not in self.int_map:
                self.int_map.append(word)

    def create_int_map(self, dataset: LetterHeaderDB) -> None:
        self.int_map = []
        for i in range(len(dataset)):
            line = dataset.get_header(i)
            self.parse_line(line)
        self.int_map = np.array(self.int_map)

    def create_token_map(self) -> None:
        self.token_map = {}
        for i in range(len(self.int_map)):
            self.token_map[self.int_map[i]] = i

    def __init__(self, word_dataset: LetterHeaderDB):
        self.int_map = []
        self.token_map = {}
        if word_dataset is not None:
            self.create_int_map(word_dataset)
            self.create_token_map()

    def get_int_from_token(self, token: str) -> int:
        return self.token_map[token]

    def get_token_from_int(self, idx: int) -> str:
        return self.int_map[idx]

    def dump(self, prefix : str) -> None:
        with open(prefix + "_token_map.json", 'w') as f:
            dump(self.token_map, f, ensure_ascii=True)

    def load(self, prefix: str) -> None:
        pass