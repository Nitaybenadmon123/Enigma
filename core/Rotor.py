from .Translator import Translator

class Rotor(Translator):
    def __init__(self, permutation: str, notch: str, ring_setting: int = 0, offset: int = 0):
        super().__init__(permutation)

        self.notch = [ord(c) - ord('A') for c in notch]
        self.ring_setting = ring_setting % 26
        self.offset = offset % 26

    def step(self):
        self.offset = (self.offset + 1) % 26

    def at_notch(self) -> bool:
        return self.offset in self.notch

    def forward(self, ch: str) -> str:
        a = self.letter_to_index(ch)

        shifted = (a + self.offset - self.ring_setting) % 26

        mapped_index = self.forward_map[shifted]

        result = (mapped_index - self.offset + self.ring_setting) % 26
        return self.index_to_letter(result)

    def reverse(self, ch: str) -> str:
        a = self.letter_to_index(ch)

        shifted = (a + self.offset - self.ring_setting) % 26

        mapped_index = self.reverse_map[shifted]

        result = (mapped_index - self.offset + self.ring_setting) % 26
        return self.index_to_letter(result)
