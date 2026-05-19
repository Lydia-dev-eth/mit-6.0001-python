# MIT 6.0001 – Problem Set 4

This repository contains my solutions for **Problem Set 4** from MIT’s *Introduction to Computer Science and Programming in Python (6.0001)*.  
The assignment explores **object‑oriented programming**, **inheritance**, and **cryptography concepts** through the design of message classes and one‑time pad encryption.

---

## 📂 Repository Structure
- `ps4a.py` – Core message shifting and pad application logic.
- `ps4b.py` – Class hierarchy for plaintext and encrypted messages.
- `ps4c.py` – Functions to test multiple pads and attempt decryption.
- `test_ps4a_student.py` – Unit tests for Part A.
- `test_ps4bc_student.py` – Unit tests for Parts B and C.
- `mit6_100l_f22_ps4.pdf` – Assignment specification.

---

## 🧩 Classes and Functions Explained

### `Message` (Base Class)
The foundation of the assignment. It represents a generic message and provides the **tools** for encryption and decryption:
- **`get_text()`** – Returns the message text safely.
- **`shift_char(char, shift)`** – Shifts a single character within the printable ASCII range `[32, 126]`. This is the core of the pad logic.
- **`apply_pad(pad)`** – Applies a one‑time pad (list of integers) to the message, producing ciphertext.

👉 Think of `Message` as the **toolbox**: it knows how to manipulate characters but doesn’t decide whether the text is plaintext or ciphertext.

---

### `PlaintextMessage` (Subclass of `Message`)
Represents a message before encryption. It adds pad management and encryption features:
- **`generate_pad()`** – Creates a random pad of the correct length.
- **`get_pad()`** – Returns a copy of the pad to avoid accidental mutation.
- **`get_ciphertext()`** – Encrypts the message by applying the pad.
- **`change_pad(new_pad)`** – Allows re‑encryption with a new pad.

👉 This class is the **author**: it takes readable text and encrypts it using a pad.

---

### `EncryptedMessage` (Subclass of `Message`)
Represents a message after encryption. It focuses on decryption:
- **`decrypt_message(pad)`** – Reverses encryption using the inverse of the pad, returning a `PlaintextMessage`.

👉 This class is the **decoder**: it takes ciphertext and, with the correct pad, recovers the original plaintext.

---

### Functions in `ps4c.py`
- **`decrypt_message_try_pads(ciphertext, pads)`**  
  Attempts to decrypt a given ciphertext using multiple candidate pads. Returns the most plausible `PlaintextMessage` (e.g., one that produces meaningful words).

👉 This function is the **detective**: it tries different keys until it finds the one that makes sense.

---

## ▶️ How to Run
Clone the repository and run the test scripts:

```bash
git clone https://github.com/Lydia-dev-eth/mit-6.0001-python.git
cd mit-6.0001-python

python test_ps4a_student.py
python test_ps4bc_student.py
