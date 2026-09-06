# DES Decryption using reversed round keys
# Requires: pycryptodome
# Install using: pip install pycryptodome

from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad


def des_decrypt(ciphertext, key):
    """
    DES decryption using the 16 round keys internally
    in reverse order: K16, K15, ..., K1.
    """

    if len(key) != 8:
        raise ValueError("DES key must be exactly 8 bytes.")

    # Create DES cipher
    cipher = DES.new(key, DES.MODE_ECB)

    # Decrypt ciphertext
    plaintext = cipher.decrypt(ciphertext)

    # Remove PKCS#5/PKCS#7 padding
    return unpad(plaintext, DES.block_size)


# ---------------- MAIN PROGRAM ----------------

print("================================")
print("       DES DECRYPTION")
print("================================")

key = input("Enter 8-character DES key: ").encode()

cipher_hex = input("Enter ciphertext in hexadecimal: ")

try:
    ciphertext = bytes.fromhex(cipher_hex)

    plaintext = des_decrypt(ciphertext, key)

    print("\nCiphertext :", cipher_hex)
    print("Key        :", key.decode())
    print("Plaintext  :", plaintext.decode())

except Exception as e:
    print("Error:", e)