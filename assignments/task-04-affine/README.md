# Task 04: Affine Cipher

## Description
This task implements the Affine Cipher, a type of monoalphabetic substitution cipher that uses mathematical functions for encryption.
It combines multiplication and addition operations to transform plaintext into ciphertext.

The Affine Cipher is more complex than the Caesar Cipher but still vulnerable to frequency analysis attacks.
It's an important example of how modular arithmetic is used in cryptography.

## Features
- Key validation (checks coprimality)
- Extended Euclidean Algorithm for modular inverse
- Case-preserving encryption/decryption
- Preserves spaces and special characters
- Automatic correctness verification

## How It Works

**Encryption Formula:**
```
E(x) = (ax + b) mod 26
```
Where:
- `x` is the letter's position (A=0, B=1, ..., Z=25)
- `a` and `b` are the key components
- `a` must be coprime with 26 (gcd(a, 26) = 1)

**Decryption Formula:**
```
D(y) = a⁻¹(y - b) mod 26
```
Where `a⁻¹` is the modular multiplicative inverse of `a` modulo 26.

**Example:**
```
Plaintext:  HELLO
Key:        (5, 8)
Ciphertext: RCLLA
```

## Implementation

**Extended GCD Algorithm:**
- Computes the greatest common divisor and coefficients for Bézout's identity
- Used to find the modular multiplicative inverse

**Key Validation:**
- Ensures `a` is coprime with 26 (gcd(a, 26) = 1)
- Invalid keys cannot be used for decryption

**Encryption:**
- Applies the affine transformation to each letter
- Preserves case and spaces

**Decryption:**
- Calculates the modular inverse of `a`
- Reverses the affine transformation
