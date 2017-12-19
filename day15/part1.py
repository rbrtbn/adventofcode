#!/usr/bin/env python3

generator_values = [883, 879]
# generator_values = [1092455, 430625591]
factors = [16807, 48271]
divisor = 2147483647  # 0b1111111111111111111111111111111

pairs = 0
matches = 0
while pairs < 5000000:
    gen_a = format(generator_values[0], 'b').zfill(32)[16:]
    gen_b = format(generator_values[1], 'b').zfill(32)[16:]
    if gen_a == gen_b:
        matches += 1

    generator_values[0] = (generator_values[0] * factors[0]) % divisor
    generator_values[1] = (generator_values[1] * factors[1]) % divisor

    pairs += 1
    # if pairs % 100000 == 0:
    #     print(pairs)

print(matches)
