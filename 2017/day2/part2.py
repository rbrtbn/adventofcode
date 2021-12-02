#!/usr/bin/env python3


def get_quotient(values):
    for i in range(len(values)):
        for j in range(i+1, len(values)):
            if values[i] > values[j]:
                dividend, divisor = values[i], values[j]
            else:
                dividend, divisor = values[j], values[i]

            if dividend % divisor == 0:
                return dividend // divisor


quotient_sum = 0
with open('input.txt') as file:
    for line in file.readlines():
        values = list(map(int, line.strip().split("\t")))
        quotient_sum += get_quotient(values)

print(quotient_sum)
