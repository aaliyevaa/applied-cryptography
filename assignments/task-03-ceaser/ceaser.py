def encrypt(plain, key):
    cipher = ''
    for ch in plain:
        if ch == ' ':
           cipher += ch
        else:
            base = ord('A') if ch.isupper() else ord('a')
            new_ind = (ord(ch) - base + key) % 26 + base
            cipher += chr(new_ind)
    return cipher

def decrypt(cipher, key):
    plain = ''
    for ch in cipher:
        if ch == ' ':
            plain += ch
        else:
            base = ord('A') if ch.isupper() else ord('a')
            new_ind = (ord(ch) - base - key) % 26 + base
            plain += chr(new_ind)
    return plain


plain = input('Enter a plain text: ')
try:
    key = int(input('Enter a shift key: '))
except ValueError:
    print('Key must be an integer')
print()

cipher = encrypt(plain, key)
print('Encrypted message: ', cipher)

dec = decrypt(cipher, key)
print('Decrypted message: ', dec)

if dec == plain:
    print('Successfully enrypted and decrypted')
else:
    print('Decrypted message is not the same as the given plain text')
