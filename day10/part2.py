#!/usr/bin/env python3

with open('input.txt') as file:
    lengths = map(ord, file.readline().strip())

lengths += [17, 31, 73, 47, 23]
# print(lengths)

marks = 256
numbers = range(marks)
current_position = 0
skip_size = 0

for _ in range(64):
    for length in lengths:
        end_position = current_position + length
        if end_position > len(numbers):
            reversed_numbers = numbers[current_position:len(numbers)] + numbers[:end_position - len(numbers)]
            reversed_numbers = reversed_numbers[::-1]
            numbers[current_position:len(numbers)] = reversed_numbers[:len(numbers) - current_position]
            numbers[:end_position - len(numbers)] = reversed_numbers[len(numbers) - current_position:]
        else:
            numbers[current_position:end_position] = numbers[current_position:end_position][::-1]

        current_position = (end_position + skip_size) % marks
        skip_size += 1

dense_hash = []
for start in range(0, 256, 16):
    hashed_value = numbers[start]
    for index in range(start + 1, start + 16):
        hashed_value ^= numbers[index]
    dense_hash.append(hashed_value)


def knot_hash(num):
    return str(hex(num))[-2:]


# print(dense_hash)
print("".join(map(knot_hash, dense_hash)))
