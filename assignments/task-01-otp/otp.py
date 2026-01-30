from random import randint 

def to_binary(text):
    result = ''
    for ch in text:
        asc = ord(ch)
        bin_asc = ''
        while asc > 0:
            bin_asc = str(asc % 2) + bin_asc
            asc //= 2
        
        while len(bin_asc) < 8:
            bin_asc = '0' + bin_asc

        result += bin_asc
    return result
    
def to_decimal(b):
    result = 0
    for i in range(len(b)):
        result += int(b[len(b)-i-1]) * (2**i)
    return result

def binary_to_text(bins):
    result = ''
    i = 0
    while i < len(bins):
        ch = bins[i:i+8]
        result += chr(to_decimal(ch))
        i += 8
    return result

def generate_key(length):
    key = ''
    for i in range(length):
        key += str(randint(0,1))
    
    return key
    
def xor(a,b): # a and b are binary strings
    result = ''
    for i in range (0,len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result


def encrypt(plain, key):
    cipher = xor(to_binary(plain),key)
    return cipher

def decrypt(cipher, key):
    plain = xor(cipher,key)
    return binary_to_text(plain)


plain = input('Enter a secret message: ')
key = generate_key(len(to_binary(plain)))
cipher = encrypt(plain, key)
print()
print('Key: ', key)
print('Encrypted: ', cipher)
print('Decrypted: ', decrypt(cipher, key))
print()
if plain == decrypt(cipher, key):
    print("Successful encryption and decryption!")
else:
    print("Decrypted message is not the same as the given plain text! ")

