from .Substitutor import Substitutor
from .Rotor import Rotor
from .Reflector import Reflector
from .Plugboard import Plugboard


class Enigma(Substitutor):
    """
    Enigma M3 machine:
    - 3 rotors: Left (L), Middle (M), Right (R)
    - 1 reflector
    - 1 plugboard
    Implements:
    - rotor stepping (including double-stepping)
    - full letter translation path
    """

    def __init__(self, left: Rotor, middle: Rotor, right: Rotor,
                 reflector: Reflector, plugboard: Plugboard):
        self.L = left
        self.M = middle
        self.R = right
        self.reflector = reflector
        self.plugboard = plugboard

    # ---------- rotor stepping (single + double step) ----------

    def _step_rotors(self):
        """
        Stepping algorithm from assignment:

        if R.notch or M.notch
          if M.notch
            advance L.offset
          advance M.offset
        advance R.offset
        """
        if self.R.at_notch() or self.M.at_notch():
            if self.M.at_notch():
                self.L.step()
            self.M.step()
        self.R.step()

    # ---------- single-letter encryption ----------

    def forward(self, ch: str) -> str:
        """
        Encrypt a single character.
        Non-letters are returned unchanged.
        """
        if not ch.isalpha():
            return ch

        ch = ch.upper()

        # step rotors before translation
        self._step_rotors()

        # 1. Plugboard in
        ch = self.plugboard.forward(ch)

        # 2. Rotors forward: R -> M -> L
        ch = self.R.forward(ch)
        ch = self.M.forward(ch)
        ch = self.L.forward(ch)

        # 3. Reflector
        ch = self.reflector.forward(ch)

        # 4. Rotors reverse: L -> M -> R
        ch = self.L.reverse(ch)
        ch = self.M.reverse(ch)
        ch = self.R.reverse(ch)

        # 5. Plugboard out
        ch = self.plugboard.forward(ch)

        return ch

    # ---------- whole-message encryption helper ----------

    def encrypt_message(self, text: str) -> str:
        """
        Encrypt a full string.
        Keeps spaces and punctuation as-is.
        """
        result = []
        for ch in text:
            if ch.isalpha():
                result.append(self.forward(ch))
            else:
                result.append(ch)
        return ''.join(result)
