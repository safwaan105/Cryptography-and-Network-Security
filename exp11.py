import math

# 25! permutations
keys = math.factorial(25)
approx_power = math.log2(keys)
print("Playfair possible keys ~ 2^", round(approx_power))

# Effective unique keys ~ 2^80
print("Effective unique keys ~ 2^80")



'''
output:
Playfair possible keys ~ 2^ 84
Effective unique keys ~ 2^80
'''