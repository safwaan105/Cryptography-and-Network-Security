# Letter Frequency Attack on Additive Cipher

text = input("Enter ciphertext: ")
n = int(input("How many possible plaintexts? "))

freq = {
    'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5,
    'I': 7.0, 'N': 6.7, 'S': 6.3, 'H': 6.1,
    'R': 6.0, 'D': 4.3, 'L': 4.0, 'C': 2.8
}

def decrypt(text, shift):
    result = ""
    for ch in text.upper():
        if ch.isalpha():
            result += chr((ord(ch) - 65 - shift) % 26 + 65)
        else:
            result += ch
    return result

def score(text):
    return sum(freq.get(ch, 0) for ch in text)

results = []

for shift in range(26):
    plain = decrypt(text, shift)
    results.append((score(plain), shift, plain))

results.sort(reverse=True)

print("\nTop", n, "possible plaintexts:\n")

for i, (score_value, shift, plain) in enumerate(results[:n], 1):
    print(i, "Shift =", shift)
    print(plain)
    print()