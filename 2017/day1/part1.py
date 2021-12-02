#!/usr/bin/env python3

captcha = 0
with open('input.txt') as file:
    digits = file.readline().strip()
    digitsLen = len(digits)
    for index in range(digitsLen):
        if digits[index] == digits[(index + 1) % digitsLen]:
            captcha += int(digits[index])

print(captcha)
