#!/usr/bin/env python3

step_per_insert = 314
circular_buffer = [0]
current_position = 0
for value in range(1, 2018):
    current_position = (current_position + step_per_insert) % len(circular_buffer) + 1
    circular_buffer.insert(current_position, value)

print(circular_buffer[(current_position + 1) % len(circular_buffer)])
