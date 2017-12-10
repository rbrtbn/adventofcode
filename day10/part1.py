#!/usr/bin/env python3

with open('input.txt') as file:
    lengths = map(int, file.readline().strip().split(','))
# lengths = [3, 4, 1, 5]

marks = 256
# marks = 5
numbers = range(marks)
current_position = 0
skip_size = 0

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

# print(numbers)
print(numbers[0] * numbers[1])
