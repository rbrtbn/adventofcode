#!/usr/bin/env python3
# import datetime

generator_values = [883, 879]
# generator_values = [1092455, 430625591]
factors = [16807, 48271]
divisor = 2147483647


def generate_a():
    generator_values[0] = (generator_values[0] * factors[0]) % divisor


def generate_b():
    generator_values[1] = (generator_values[1] * factors[1]) % divisor


def generate_values_matching_criteria():
    while generator_values[0] & 0b11 != 0:
        generate_a()

    while generator_values[1] & 0b111 != 0:
        generate_b()

    return generator_values[0], generator_values[1]


pairs = 0
matches = 0
while pairs < 5000000:
    a, b = generate_values_matching_criteria()

    if (a & 0xFFFF) ^ (b & 0xFFFF):
        matches += 1

    pairs += 1
    generate_a()
    generate_b()
    # if pairs % 100000 == 0:
    #     print(pairs, datetime.datetime.now())

print(matches)
