#!/usr/bin/env python3
from blist import blist

step_per_insert = 314
circular_buffer = blist([0])
current_position = 0
for value in range(1, 50000000):
    current_position = (current_position + step_per_insert) % len(circular_buffer) + 1
    circular_buffer.insert(current_position, value)
    # if value % 100000 == 0:
    #     print(value)

print(circular_buffer[1])
