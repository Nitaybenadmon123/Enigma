📘 Enigma Machine Emulator – Software Safety – Homework 1

Authors:

Nitay Ben Admon

Idan Tegave

Course: Software Safety
Institution: SCE
Semester: 2025

🚀 Overview

This project is a full emulator of the German Enigma M3 cipher machine, implemented according to the requirements of Homework 1.
The emulator supports:

Plugboard (Steckerbrett)

Rotors with wiring, ring settings, offsets, and notches

Full stepping mechanism including double stepping

Reflector (Umkehrwalze B)

Full forward/reverse signal path

Message-key encryption & recovery (Task 5)


Performance benchmarking (Task 6)

The implementation was validated using the test cases given in the assignment.




📂 Project Structure

Enigma/
│
├── core/
│   ├── Substitutor.py
│   ├── Translator.py
│   ├── Rotor.py
│   ├── Reflector.py
│   ├── Plugboard.py
│   └── Enigma.py
│
├── main.py
└── README.md


🧩 Core Components
Substitutor

Base class providing alphabet utilities:

letter_to_index(ch)

index_to_letter(i)



Translator

Stores a forward permutation and automatically computes the inverse permutation.

Used as the parent class of:

Rotor

Reflector



Rotor

Implements an authentic Enigma rotor:

Internal wiring

Ring setting (Ringstellung)

Rotor offset (Grundstellung)

Notch position

Forward & reverse signal paths

Mechanical stepping

Double-stepping behavior

Mathematical rules:

Forward: P( A + offset − ring ) − offset + ring
Reverse: P⁻¹( A + offset − ring ) − offset + ring


Plugboard

Supports up to 10 swapping pairs.
Symmetric mapping: if A→C then C→A.

Reflector

Implements Reflector B.
Mapping is symmetric and identical in both directions.

Enigma Machine

Coordinates all components in correct order:

1. Step rotors (with double stepping)
2. Plugboard input
3. Rotors forward (Right → Middle → Left)
4. Reflector bounce
5. Rotors backward (Left → Middle → Right)
6. Plugboard output


🧪 Task 4 – Validation Against Assignment Table

Assignment test case (first row):

Rotors: I-II-III

Ring setting: A-A-A

Initial offsets: F-D-V

Reflector: B

Plugboard: empty

Input: ENIGMA

Expected output: QGELID


Input     : ENIGMA
Output    : QGELID
Expected  : QGELID
✔ Passed successfully.

🔐 Task 5 – Decrypting the Historical Message

The program:

Uses ground setting G = DOR

Decrypts the encrypted message key E(K, G)

Recovers K = DOR

Reinitializes the machine using offset = K

Decrypts the message

Output:
Recovered message key K: DOR

Plaintext message:
GROUPSOUTHCOMMANDFROMGENPAULUSXSIXTHARMYISENCIRCLEDXOPERATIONBLAUFAILEDXCOMMENCERELIEFOPERATIONIMMEDIATELY
✔ Matches the historically correct plaintext.


⚡ Task 6 – Performance Benchmark

Using Python’s cProfile:
3,414,002 function calls in 1.673 seconds
Typical performance for a full Python implementation of Enigma.

▶ Running the Project

Run the project with:
python main.py


📌 Conclusion

This project provides:

A complete and accurate simulation of the Enigma M3

Full support for all mechanisms, including double stepping

Correct results for all assignment test cases

Successful decryption of the Task 5 message

Verified performance metrics

Both authors contributed to design, implementation, and validation.
