from .Substitutor import Substitutor

class Plugboard(Substitutor):
    """
    Plugboard: swaps paired letters (A<->F, B<->Z, ...)
    Non-paired letters map to themselves.
    """

    def __init__(self, pairs=None):
        # Create mapping A->A, B->B, ..., Z->Z
        self.map = {
            self.index_to_letter(i): self.index_to_letter(i)
            for i in range(26)
        }

        # Apply plugboard swaps
        if pairs:
            for a, b in pairs:
                self.map[a] = b
                self.map[b] = a

    def forward(self, ch: str) -> str:
        """Return swapped letter."""
        return self.map[ch]
