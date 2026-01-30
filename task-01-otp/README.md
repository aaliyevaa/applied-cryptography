# Task 01: One-Time Pad (OTP)

## Description
This task implements One-Time Pad (OTP) encryption in Python.
The program converts plaintext to binary, generates a random key of equal length, and performs XOR-based encryption and decryption.

OTP is a provably secure encryption method which is theoretically unbreakable when the key is truly random, never reused, and kept secret.

## Features 

1. Convert a string message to Unicode numbers.
2. Convert Unicode numbers to binary representation.
3. Generate a random binary key equal in length to the binary message.
4. Encrypt the message using bitwise XOR with the key.
5. Decrypt the message using the same key.
6. Verify that the decrypted message matches the original.

## How It Works

1. **Text to Binary**  
Each character is converted to ASCII, then manually converted to 8-bit binary representation.

2. **Key Generation**  
A random binary key is generated matching the message length (each bit randomly 0 or 1).

3. **Encryption and Decryption**  
The binary message and key are XORed bit-by-bit to produce the ciphertext.
XORing the ciphertext with the same key recovers the original message.

```
0 ⊕ 0 = 0    1 ⊕ 0 = 1
0 ⊕ 1 = 1    1 ⊕ 1 = 0
```

4. **Verification**  
The program confirms the decrypted message matches the original plaintext.

