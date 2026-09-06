import string
from collections import Counter

# English letter frequency (most common to least common)
ENGLISH_FREQ = "ETAOINSHRDLCUMWFGYPBVKJXQZ"


def letter_frequency_attack(ciphertext, top_n=10):
    # Count letters in ciphertext
    frequency = Counter(
        c.upper() for c in ciphertext if c.isalpha()
    )

    # Sort cipher letters by frequency
    cipher_freq = [letter for letter, count in frequency.most_common()]

    # Complete alphabet if some letters are missing
    for letter in string.ascii_uppercase:
        if letter not in cipher_freq:
            cipher_freq.append(letter)

    results = []

    # Try different frequency shifts
    # This generates possible substitution mappings
    for shift in range(26):
        mapping = {}

        for i, cipher_letter in enumerate(cipher_freq):
            plain_letter = ENGLISH_FREQ[(i + shift) % 26]
            mapping[cipher_letter] = plain_letter

        plaintext = ""

        for char in ciphertext:
            if char.upper() in mapping:
                decrypted = mapping[char.upper()]
                plaintext += decrypted if char.isupper() else decrypted.lower()
            else:
                plaintext += char

        # Calculate a simple score based on common English words
        score = english_score(plaintext)
        results.append((score, plaintext))

    # Remove duplicate plaintexts and sort by likelihood
    results = sorted(set(results), reverse=True)

    return results[:top_n]


def english_score(text):
    # Common English words used for scoring
    common_words = [
        "THE", "AND", "THAT", "THIS", "WITH",
        "FROM", "HAVE", "FOR", "ARE", "WAS",
        "YOU", "NOT", "BUT", "ALL", "CAN",
        "HELLO", "IS", "TO", "OF", "IN"
    ]

    score = 0

    upper_text = text.upper()

    for word in common_words:
        score += upper_text.count(word) * len(word)

    return score


# ---------------- MAIN PROGRAM ----------------

print("MONOALPHABETIC SUBSTITUTION CIPHER")
print("-----------------------------------")

ciphertext = input("Enter ciphertext: ")

try:
    top_n = int(input("How many possible plaintexts? "))
except ValueError:
    top_n = 10

results = letter_frequency_attack(ciphertext, top_n)

print("\nPossible plaintexts:")
print("-------------------")

for i, (score, plaintext) in enumerate(results, 1):
    print(f"{i}. {plaintext}")