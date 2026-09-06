import numpy as np

key = np.array([[9,4],[5,7]])
msg = "meetmeattheusualplaceattenratherthaneightoclock"
msg = msg.replace(" ", "")

cipher = ""
for i in range(0, len(msg), 2):
    a = ord(msg[i]) - ord('a')
    b = ord(msg[i+1]) - ord('a')
    vec = np.array([a,b])
    res = key.dot(vec) % 26
    cipher += chr(res[0]+ord('a')) + chr(res[1]+ord('a'))
print("Ciphertext:", cipher)



'''
output:
Ciphertext: qtxxgqzqfwnzqzqzqfwnzqzqzqfwnzqzqzqfwnzqzqzqfwnzqzqzqfwnzqzqzqfwnzqzqzqfwnzqzqzq
'''