from core.Rotor import Rotor
from core.Reflector import Reflector
from core.Plugboard import Plugboard
from core.Enigma import Enigma
import cProfile
import pstats
def build_enigma():
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

    # Reflector
    reflector_B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")

    # Empty plugboard (לפי הטבלה)
    plugboard = Plugboard([])

    # Create machine – using your constructor format
    return Enigma(
        left=rotor_I,
        middle=rotor_II,
        right=rotor_III,
        reflector=reflector_B,
        plugboard=plugboard
    )
def benchmark():
    msg = "HELLOWORLD"
    for _ in range(2000):   # כמות נכבדת לבדיקה
        enigma = build_enigma()
        enigma.encrypt_message(msg)
def run_profile():
    profiler = cProfile.Profile()
    profiler.enable()

    benchmark()

    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats("tottime")
    stats.print_stats(25)   # מציג את 25 הפונקציות הכי כבדות



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
    # Rotor IIII
    rotor_IIII = Rotor(
        permutation="ESOVPZJAYQUIRHXLNFTGKDCMWB",
        notch="J",
        ring_setting=0,
        offset=0
    )
    # Rotor IIIII
    rotor_IIIII = Rotor(
        permutation="VZBRGITYUPSDNHLXAWMJQOFECK",
        notch="Z",
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
    # main()            # זה מריץ את התרגיל הרגיל שלך
    run_profile()        # זה מפעיל את בדיקת הביצועים (Task 6)
    