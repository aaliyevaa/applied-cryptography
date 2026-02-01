def gcd(a,b):
    if b == 0:
        return a
    if a == 0:
        return b
    return gcd(b, a % b)
