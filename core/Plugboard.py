from .Substitutor import Substitutor

class Plugboard(Substitutor):
    """
    Plugboard supports up to 10 pairs.
    Provides:
    - forward(): swap letters
    - reverse(): identical to forward()
    - get_permutation(): return full 26-letter permutation
    """

    def __init__(self, pairs=None):
        if pairs is None:
            pairs = []

        # שמירת מיפוי קדימה ואחורה
        self.map = {}

        for a, b in pairs:
            a = a.upper()
            b = b.upper()
            self.map[a] = b
            self.map[b] = a

        # בניית הפרמוטציה המלאה
        perm = []
        for i in range(26):
            ch = chr(ord('A') + i)
            perm.append(self.map.get(ch, ch))
        self.permutation = ''.join(perm)

    def forward(self, ch: str) -> str:
        return self.map.get(ch.upper(), ch.upper())

    def reverse(self, ch: str) -> str:
        return self.forward(ch)

    def get_permutation(self):
        return self.permutation
