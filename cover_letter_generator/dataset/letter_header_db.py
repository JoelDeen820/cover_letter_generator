import numpy as np


class LetterHeaderDB(object):

    def __init__(self, filename):
        self.table = []
        with open(filename) as f:
            for line in f:
                self.table.append(line.strip().lower())

    def get_header(self, key: int) -> str:
        return self.table[key]

    def __getitem__(self, item) -> str:
        return self.get_header(item)

    def __len__(self) -> int:
        return len(self.table)