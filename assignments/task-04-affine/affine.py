def extended_gcd(a,b):
    if b == 0:
        return a, 1, 0
    
    gcd, x1, y1 = extended_gcd(b, a %b)

    x = y1
    y = x1 - (a//b)*y1

    return gcd, x, y

def key_validation(key):
    a = key[0]
    gcd, _, _ = extended_gcd(a, 26)
    if gcd == 1:
        return True
    return False

def inverse(a):
    _, x, _ = extended_gcd(a, 26)
    return x % 26

def encrypt(plain, key):
    a,b = key
    cipher = ''
    for ch in plain:
        if ch == ' ':
            cipher += ch
        else:
            base = ord('A') if ch.isupper() else ord('a')
            new_ind = ((ord(ch) - base) * a + b) % 26
            cipher += chr(new_ind + base)
    return cipher

def decrypt(cipher, key):
    plain = ''
    a,b = key
    for ch in cipher:
        if ch == ' ':
            plain += ch
        else:
            base = ord('A') if ch.isupper() else ord('a')
            new_ind = ((ord(ch) - base - b) * inverse(a)) % 26
            plain += chr(new_ind + base)
    return plain

plain = input('Enter a message: ')
a, b = map(int, input("Enter key  (x y): ").split())
key = (a, b)
if not key_validation(key):
    print(f"Invalid key.\ngcd({b}, 26) must be 1")
else:
    cipher = encrypt(plain,key)
    print('Encrpyted: ', cipher)
    dec = decrypt(cipher,key)
    if dec == plain:
        print('Successfull encryption and decryption')
    else:
        print('Decrypted message is not the same as given plaintext')
