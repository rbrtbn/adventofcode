#!/usr/bin/env python3

# reg_b = 65 * 100 + 100000
# reg_c = reg_b + 17000
# reg_h = 0
# while True:
#     reg_f = 1
#     reg_d = 2
#     while True:
#         reg_e = 2
#         while True:
#             reg_g = reg_d * reg_e - reg_b
#             if reg_g == 0:
#                 reg_f = 0
#             reg_e += 1
#             reg_g = reg_e - reg_b
#             if reg_g == 0:
#                 break
#         reg_d += 1
#         reg_g = reg_d - reg_b
#         if reg_g == 0:
#             break
#     if reg_f == 0:
#         reg_h += 1
#     reg_g = reg_b - reg_c
#     if reg_g == 0:
#         break
#     reg_b += 17

import sympy

non_primes = 0
for num in range(106500, 123500+1, 17):
    if not sympy.isprime(num):
        non_primes += 1

print(non_primes)