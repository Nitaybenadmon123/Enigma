from .Translator import Translator

class Reflector(Translator):
    """
    Reflector: symmetric mapping (A<->Y, B<->R, ...)
    Reverse = forward
    """

    def forward(self, ch: str) -> str:
        """Reflect the letter using the forward mapping."""
        idx = self.letter_to_index(ch)
        return self.forward_map[idx]

    def reverse(self, ch: str) -> str:
        """Reflectors are symmetric: reverse == forward."""
        return self.forward(ch)
