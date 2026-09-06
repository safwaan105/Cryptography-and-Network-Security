import numpy as np

# Example plaintext-ciphertext pairs
P = np.array([[0,12],[19,4]])   # plaintext numbers
C = np.array([[8,5],[11,19]])   # ciphertext numbers

# Inverse of P mod 26
det = int(np.round(np.linalg.det(P)))
det_inv = pow(det, -1, 26)  # modular inverse
adj = np.array([[P[1,1], -P[0,1]], [-P[1,0], P[0,0]]])
P_inv = (det_inv * adj) % 26

K = (C.dot(P_inv)) % 26
print("Recovered key matrix:\n", K)


'''
output:
Recovered key matrix:
 [[ 7  8]
 [ 5 10]]
'''