from cover_letter_generator.dataset.letter_header_db import LetterHeaderDB


class SequenceGenerator:

    def generate_sequence(self, line: str) -> list[str]:
        split_line = line.split()
        if len(split_line) > self.sequence_length:
            sequences = []
            for i in range(self.sequence_length, len(split_line)):
                seq = split_line[i - self.sequence_length: i + 1]
                sequences.append(" ".join(seq))
            return sequences
        else:
            return [line]

    def generate_sequences(self):
        sequences = []
        for i in range(len(self.dataset)):
            line = self.dataset[i]
            sequences.append(self.generate_sequence(line))
        self.sequences = sum(sequences, [])

    def __init__(self, sequence_len=5, dataset=None, input_sequences=None):
        self.sequences = []
        self.sequence_length = sequence_len
        if dataset is not None:
            if isinstance(dataset, LetterHeaderDB):
                self.dataset = dataset
                self.generate_sequences()
            else:
                raise ValueError
        elif input_sequences is not None:
            if isinstance(input_sequences, list):
                self.sequences = input_sequences.copy()
            else:
                raise ValueError

    def __eq__(self, other):
        if isinstance(other, SequenceGenerator):
            return other.sequences == self.sequences
        else:
            return False

    def __getitem__(self, item: int) -> str:
        return self.sequences[item]

    def __len__(self) -> int:
        return len(self.sequences)

    def generate_labeled_data(self) -> tuple[list[str], list[str]]:
        x: list[str] = []
        y: list[str] = []
        for sequence in self.sequences:
            x.append(" ".join(sequence.split()[:-1]))
            y.append(" ".join(sequence.split()[1:]))
        return x, y

    def get_sequence_list(self) -> list[str]:
        return self.sequences
