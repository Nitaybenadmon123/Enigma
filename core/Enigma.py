from .Substitutor import Substitutor
from .Rotor import Rotor
from .Reflector import Reflector
from .Plugboard import Plugboard


class Enigma(Substitutor):
    """
    Enigma M3 machine (Task 4).
    Inherits from Substitutor, as required in Task 1.

    Components:
    - Plugboard (Substitutor)
    - 3 Rotors (Left, Middle, Right)
    - Reflector
    - Implements stepping + double stepping
    """

    def __init__(self, left: Rotor, middle: Rotor, right: Rotor,
                 reflector: Reflector, plugboard: Plugboard):
        self.L = left
        self.M = middle
        self.R = right
        self.reflector = reflector
        self.plugboard = plugboard

    # -----------------------------------
    # ROTOR STEPPING (with double stepping)
    # -----------------------------------
    def _step_rotors(self):
        """
        Task 4 stepping rules:

        if R.notch or M.notch:
            if M.notch:
                step L
            step M
        step R
        """

        if self.R.at_notch() or self.M.at_notch():
            if self.M.at_notch():
                self.L.step()
            self.M.step()

        self.R.step()

    # -----------------------------------
    # ENCRYPT A SINGLE CHARACTER
    # -----------------------------------
    def forward(self, ch: str) -> str:
        """
        Encrypt a single letter.
        Non-letters are returned unchanged.
        """

        if not ch.isalpha():
            return ch

        ch = ch.upper()

        # 1. Step rotors
        self._step_rotors()

        # 2. Plugboard in
        ch = self.plugboard.forward(ch)

        # 3. Rotors forward (R → M → L)
        ch = self.R.forward(ch)
        ch = self.M.forward(ch)
        ch = self.L.forward(ch)

        # 4. Reflector
        ch = self.reflector.reflect(ch)

        # 5. Rotors backward (L → M → R)
        ch = self.L.reverse(ch)
        ch = self.M.reverse(ch)
        ch = self.R.reverse(ch)

        # 6. Plugboard out
        ch = self.plugboard.forward(ch)

        return ch

    # -----------------------------------
    # FULL MESSAGE ENCRYPTION
    # -----------------------------------
    def encrypt_message(self, text: str) -> str:
        result = []
        for ch in text:
            result.append(self.forward(ch) if ch.isalpha() else ch)
        return ''.join(result)

    # Assignment compatibility
    def encrypt(self, text: str) -> str:
        return self.encrypt_message(text)
