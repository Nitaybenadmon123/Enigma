from core.Rotor import Rotor
from core.Reflector import Reflector
from core.Plugboard import Plugboard
from core.Enigma import Enigma


def main():

    # Rotors I-II-III
    rotor_I = Rotor(
        permutation="EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        notch="Q",
        ring_setting=2,
        offset=18    # F
    )

    rotor_II = Rotor(
        permutation="AJDKSIRUXBLHWTMCQGZNPYFVOE",
        notch="E",
        ring_setting=7,
        offset=3    # D
    )

    rotor_III = Rotor(
        permutation="BDFHJLCPRTXVZNYEIWGAKMUSQO",
        notch="V",
        ring_setting=5,
        offset=8   # V
    )

    # Reflector B
    reflector_B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")

    # Plugboard: empty
    plugboard = Plugboard([("A","T"),("C","E"),("R","L")])

    # Enigma machine
    enigma = Enigma(
        left=rotor_I,
        middle=rotor_II,
        right=rotor_III,
        reflector=reflector_B,
        plugboard=plugboard
    )

    plaintext = "PEACE"
    ciphertext = enigma.encrypt(plaintext)

    print("Expected: ISWAR")
    print("Actual  :", ciphertext)


if __name__ == "__main__":
    main()
