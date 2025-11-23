# main.py

from core.Rotor import Rotor
from core.Reflector import Reflector
from core.Plugboard import Plugboard
from core.Enigma import Enigma
def run_table_test():
    # Rotors I-II-III
    rotor_I = Rotor(
        permutation="EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        notch="Q",
        ring_setting=0,
        offset=5   # F = 6 → offset=5
    )

    rotor_II = Rotor(
        permutation="AJDKSIRUXBLHWTMCQGZNPYFVOE",
        notch="E",
        ring_setting=0,
        offset=3   # D = 4 → offset=3
    )

    rotor_III = Rotor(
        permutation="BDFHJLCPRTXVZNYEIWGAKMUSQO",
        notch="V",
        ring_setting=0,
        offset=21  # V = 22 → offset=21
    )

    reflector_B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
    plugboard = Plugboard([])  # empty

    enigma = Enigma(
        rotor_I, rotor_II, rotor_III,
        reflector=reflector_B,
        plugboard=plugboard
    )

    plaintext = "ENIGMA"
    ciphertext = enigma.encrypt(plaintext)

    print("Input     :", plaintext)
    print("Output    :", ciphertext)
    print("Expected  : QGELID")


def build_enigma():
    # רוטורים II, V, IV
    rotor_II  = Rotor(permutation="AJDKSIRUXBLHWTMCQGZNPYFVOE", notch="E", ring_setting=19-1, offset=0)
    rotor_V   = Rotor(permutation="VZBRGITYUPSDNHLXAWMJQOFECK", notch="Z", ring_setting=9-1,  offset=0)
    rotor_IV  = Rotor(permutation="ESOVPZJAYQUIRHXLNFTGKDCMWB", notch="J", ring_setting=24-1, offset=0)

    plugboard = Plugboard([
        ("Z","U"), ("H","L"), ("C","Q"), ("W","M"),
        ("O","A"), ("P","Y"), ("E","B"), ("T","R"),
        ("D","N"), ("V","I")
    ])
    reflector_B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")

    return Enigma(left=rotor_II, middle=rotor_V, right=rotor_IV,
                  reflector=reflector_B, plugboard=plugboard)


def set_offsets(enigma, offsets: str):
    # offsets כמו "C O N"
    offs = offsets.replace(" ", "")
    enigma.L.offset = ord(offs[0]) - ord('A')
    enigma.M.offset = ord(offs[1]) - ord('A')
    enigma.R.offset = ord(offs[2]) - ord('A')


def main():
    enigma = build_enigma()

    # נתונים מהמשימה
    G = "CON"    # Ground setting
    E_KG = "MLD" # E(K,G) — מפתח הודעה מוצפן

    # שלב 1: הצבת רוטורים ל-G
    set_offsets(enigma, G)

    # שלב 2: פענוח מפתח ההודעה
    K = enigma.encrypt(E_KG)
    print("Recovered message key K:", K)

    # שלב 3: הצבת הרוטורים למפתח ההודעה
    set_offsets(enigma, K)

    # שלב 4: פענוח ההודעה עצמה (הסר YHP וקבוצת הזיהוי)
    ciphertext = (
        "UMDPQCUAQNLVVSP"
        "IARKCTTRJQKCFPTOKRGO"
        "ZXALDRLPUHAUZSOSZFSU"
        "GWFNFDZCUGVEXUULQYXO"
        "TCYRP SYGGZ HQMAG PZDKC"
        "KGOJMMYYDDH"
    ).replace(" ", "")
    plaintext = enigma.encrypt(ciphertext)
    print("Plaintext message:", plaintext)
    #כגעגעגעיי



if __name__ == "__main__":
    main()
    run_table_test()
