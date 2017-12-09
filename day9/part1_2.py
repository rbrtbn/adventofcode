#!/usr/bin/env python3

with open('input.txt') as file:
    line = file.readline().strip()

    group_score = 0
    total_score = 0
    garbage = False
    skip_next = False
    garbage_length = 0
    for char in line:
        if garbage:
            if skip_next:
                skip_next = False
            elif char == '!':
                skip_next = True
            elif char == '>':
                garbage = False
            else:
                garbage_length += 1
        elif char == '{':
            group_score += 1
        elif char == '}':
            total_score += group_score
            group_score -= 1
        elif char == ',':
            continue
        elif char == '<':
            garbage = True

print(total_score)
print(garbage_length)
