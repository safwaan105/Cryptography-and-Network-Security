# One-Time Pad Vigenere Cipher

import string

A = string.ascii_lowercase

def encrypt(text, key):
    text = text.replace(" ", "").lower()
    return ''.join(A[(A.index(p) + k) % 26]
                   for p, k in zip(text, key))

def decrypt(text, key):
    return ''.join(A[(A.index(c) - k) % 26]
                   for c, k in zip(text, key))


# (a)
plaintext = "send more money"
key = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]

cipher = encrypt(plaintext, key)

print("Ciphertext:", cipher)


# (b)
new_plaintext = "cash not needed"
new_plaintext = new_plaintext.replace(" ", "")

new_key = [(A.index(c) - A.index(p)) % 26
           for c, p in zip(cipher, new_plaintext)]

print("New Key:", new_key)
print("Decrypted:", decrypt(cipher, new_key))