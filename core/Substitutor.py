from abc import ABC, abstractmethod

class Substitutor(ABC):
    """
    Abstract base class for all substitution components.
    Provides:
    - letter <-> index conversion
    - circular shifting
    - abstract forward() for translation
    - default reverse() (symmetric unless overridden)
    """

    @staticmethod
    def letter_to_index(ch: str) -> int:
        """Convert A–Z to 0–25."""
        return ord(ch.upper()) - ord('A')

    @staticmethod
    def index_to_letter(i: int) -> str:
        """Convert 0–25 to A–Z."""
        return chr((i % 26) + ord('A'))

    @staticmethod
    def shift_index(i: int, amount: int) -> int:
        """Shift index circularly (mod 26)."""
        return (i + amount) % 26

    @abstractmethod
    def forward(self, ch: str) -> str:
        """Abstract forward translation."""
        pass

    def reverse(self, ch: str) -> str:
        """
        Default reverse translation.
        Used for symmetric mappings (plugboard, reflector, Enigma wrapper).
        """
        return self.forward(ch)
