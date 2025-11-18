from core.Rotor import Rotor
from core.Reflector import Reflector
from core.Plugboard import Plugboard
from core.Enigma import Enigma


def main():
    # ----------------------------
    # 1. הגדרת הרוטורים
    # ----------------------------

    # Rotor I
    rotor_I = Rotor(
        permutation="EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        notch="Q",
        ring_setting=0,
        offset=0
    )

    # Rotor II
    rotor_II = Rotor(
        permutation="AJDKSIRUXBLHWTMCQGZNPYFVOE",
        notch="E",
        ring_setting=0,
        offset=0
    )

    # Rotor III
    rotor_III = Rotor(
        permutation="BDFHJLCPRTXVZNYEIWGAKMUSQO",
        notch="V",
        ring_setting=0,
        offset=0
    )

    # ----------------------------
    # 2. רפלקטור B
    # ----------------------------
    reflector_B = Reflector(
        permutation="YRUHQSLDPXNGOKMIEBFZCWVJAT"
    )

    # ----------------------------
    # 3. פלגבורד (אפשר להשאיר ריק)
    # ----------------------------
    plugboard = Plugboard([
        ("A", "B"),
        ("C", "D")
    ])

    # ----------------------------
    # 4. יצירת המכונה
    # סדר רוטורים: Left, Middle, Right
    # ----------------------------
    enigma = Enigma(
        left=rotor_I,
        middle=rotor_II,
        right=rotor_III,
        reflector=reflector_B,
        plugboard=plugboard
    )

    # ----------------------------
    # 5. הצפנת הודעה
    # ----------------------------
    plaintext = "HH"
    ciphertext = enigma.encrypt_message(plaintext)

    print("Plaintext :", plaintext)
    print("Ciphertext:", ciphertext)


if __name__ == "__main__":
    main()
