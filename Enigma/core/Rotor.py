from .Translator import Translator
from .Substitutor import Substitutor

class Rotor(Translator):
    """
    Rotor:
    - Has a forward and reverse permutation (inherited from Translator)
    - Has a ring setting (Ringstellung)
    - Has an offset (position shown in the window)
    - Has a notch (causes the next rotor to step)
    """

    def __init__(self, permutation: str, notch: str, ring_setting: int = 0, offset: int = 0):
        super().__init__(permutation)
        self.notch = notch
        self.ring_setting = ring_setting
        self.offset = offset

    def at_notch(self) -> bool:
        """Check if rotor is currently at notch position."""
        return self.index_to_letter(self.offset) == self.notch

    def step(self):
        """Rotate rotor by 1 position."""
        self.offset = (self.offset + 1) % 26

    def forward(self, ch: str) -> str:
        """Forward pass through rotor wiring with ring and offset."""
        i = self.letter_to_index(ch)
        i = self.shift_index(i, self.offset - self.ring_setting)
        mapped = self.forward_map[i]
        i2 = self.letter_to_index(mapped)
        i2 = self.shift_index(i2, -self.offset + self.ring_setting)
        return self.index_to_letter(i2)

    def reverse(self, ch: str) -> str:
        """Reverse pass through rotor wiring."""
        i = self.letter_to_index(ch)
        i = self.shift_index(i, self.offset - self.ring_setting)
        mapped = self.reverse_map[i]
        i2 = self.letter_to_index(mapped)
        i2 = self.shift_index(i2, -self.offset + self.ring_setting)
        return self.index_to_letter(i2)
