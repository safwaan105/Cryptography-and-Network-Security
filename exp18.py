# DES KEY GENERATION
# Generates 16 DES subkeys of 48 bits each
# No external libraries required


# PC-1: 64-bit key -> 56-bit key
PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]


# PC-2: 56-bit key -> 48-bit subkey
PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]


# DES left-shift schedule
SHIFT = [
    1, 1, 2, 2, 2, 2, 2, 2,
    1, 2, 2, 2, 2, 2, 2, 1
]


def permute(key, table):
    """Perform permutation according to the given table."""
    return ''.join(key[i - 1] for i in table)


def left_shift(bits, n):
    """Circular left shift."""
    return bits[n:] + bits[:n]


def generate_subkeys(key64):

    # Step 1: Apply PC-1
    key56 = permute(key64, PC1)

    # Step 2: Split into two 28-bit halves
    C = key56[:28]
    D = key56[28:]

    subkeys = []

    print("\nInitial 56-bit key:")
    print(key56)

    print("\nC0 =", C)
    print("D0 =", D)

    # Step 3: Generate 16 subkeys
    for round_no in range(16):

        # Shift C and D
        C = left_shift(C, SHIFT[round_no])
        D = left_shift(D, SHIFT[round_no])

        # Combine C and D
        combined = C + D

        # Step 4: Apply PC-2
        subkey = permute(combined, PC2)

        subkeys.append(subkey)

        print("\nRound", round_no + 1)
        print("C" + str(round_no + 1), "=", C)
        print("D" + str(round_no + 1), "=", D)
        print("K" + str(round_no + 1), "=", subkey)

    return subkeys


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------

print("========================================")
print("        DES KEY GENERATION")
print("========================================")

key = input("Enter 64-bit binary key: ")

# Validate input
if len(key) != 64:
    print("Error: Key must contain exactly 64 bits.")
elif any(bit not in "01" for bit in key):
    print("Error: Key must contain only 0 and 1.")
else:

    subkeys = generate_subkeys(key)

    print("\n========================================")
    print("          DES SUBKEYS")
    print("========================================")

    for i, subkey in enumerate(subkeys, 1):
        print("K" + str(i) + " =", subkey)