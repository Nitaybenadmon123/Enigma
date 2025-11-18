from abc import abstractmethod
from .Substitutor import Substitutor

class Translator(Substitutor):
    """
    Abstract translator that stores a forward permutation
    and automatically computes the reverse permutation.
    """

    def __init__(self, permutation: str):
        self.forward_map = permutation

        # Build reverse permutation automatically
        self.reverse_map = [''] * 26
        for i, ch in enumerate(permutation):
            index = Substitutor.letter_to_index(ch)
            self.reverse_map[index] = Substitutor.index_to_letter(i)

        self.reverse_map = ''.join(self.reverse_map)

    @abstractmethod
    def forward(self, ch: str) -> str:
        """Translate a letter forward."""
        pass

    def reverse(self, ch: str) -> str:
        """Use the precomputed reverse permutation."""
        idx = self.letter_to_index(ch)
        return self.reverse_map[idx]
