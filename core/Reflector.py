from .Translator import Translator

class Reflector(Translator):
    """
    Reflector (Umkehrwalze):
    Always symmetric.
    """

    def __init__(self, permutation: str):
        super().__init__(permutation)

    def reflect(self, ch: str) -> str:
        idx = self.letter_to_index(ch)

        # forward_map gives an INDEX now, not a letter
        mapped_index = self.forward_map[idx]

        # must convert back to LETTER
        return self.index_to_letter(mapped_index)

    def forward(self, ch: str) -> str:
        return self.reflect(ch)

    def reverse(self, ch: str) -> str:
        return self.reflect(ch)
