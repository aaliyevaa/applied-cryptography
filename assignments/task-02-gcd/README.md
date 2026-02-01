# Task 02: Greatest Common Divisor (GCD) using Euclidean Algorithm

## Description
This task implements the Euclidean Algorithm to compute the Greatest Common Divisor (GCD) of two integers. The GCD is the largest positive integer that divides both numbers without a remainder.

The Euclidean Algorithm is one of the oldest algorithms in mathematics and is fundamental to many cryptographic operations, including finding modular multiplicative inverses and working with RSA encryption.

**Euclidean Algorithm**  
The algorithm is based on the principle that:
```
gcd(a, b) = gcd(b, a mod b)
```

The process repeats recursively until one number becomes 0, at which point the other number is the GCD.

**Example:**
```
gcd(48, 18)
= gcd(18, 48 mod 18)
= gcd(18, 12)
= gcd(12, 6)
= gcd(6, 0)
= 6
```

## Features
- Recursive implementation
- Handles edge cases (zero values)

  
## How it works
The function uses recursion:
- **Base cases:** If either number is 0, return the other number
- **Recursive case:** Replace the larger number with the remainder of division



