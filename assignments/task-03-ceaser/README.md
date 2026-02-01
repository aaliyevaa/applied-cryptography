# Task 03: Caesar Cipher

## Description
This task implements the Caesar Cipher, one of the simplest and oldest encryption techniques. It works by shifting each letter in the plaintext by a fixed number of positions in the alphabet.

The Caesar Cipher is named after Julius Caesar, who used it to protect military messages. While not secure by modern standards, it demonstrates fundamental concepts in substitution ciphers.

## Features
- Case-preserving encryption/decryption
- Handles wrap-around (Z → A)
- Preserves spaces and special characters
- Input validation for the shift key

## How It Works

**Encryption**  
- Preserves spaces and non-alphabetic characters
- Handles both uppercase and lowercase letters
- Uses modulo 26 to wrap around the alphabet
- Each letter is shifted forward in the alphabet by the key value:
  - `A` with key 3 becomes `D`
  - `Z` with key 3 wraps around to `C`

**Decryption**  
- Reverses the shift by subtracting the key

**Example:**
```
Plaintext:  HELLO WORLD
Key:        3
Ciphertext: KHOOR ZRUOG
```

**Verification:**
- Confirms the decrypted message matches the original plaintext
