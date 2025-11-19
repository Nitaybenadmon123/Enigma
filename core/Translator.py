from abc import abstractmethod
from .Substitutor import Substitutor

class Translator(Substitutor):
    """
    Stores forward permutation as numeric LIST (indexes 0–25)
    and builds reverse permutation also as numeric LIST.
    """

    def __init__(self, permutation: str):
        # Convert permutation letters → numbers
        self.forward_map = [Substitutor.letter_to_index(ch) for ch in permutation]

        # Build reverse map as numbers
        self.reverse_map = [0] * 26
        for i, ch in enumerate(permutation):
            target_index = Substitutor.letter_to_index(ch)
            self.reverse_map[target_index] = i

    @abstractmethod
    def forward(self, ch: str) -> str:
        pass

    def reverse(self, ch: str) -> str:
        idx = self.letter_to_index(ch)
        mapped_index = self.reverse_map[idx]
        return self.index_to_letter(mapped_index)
