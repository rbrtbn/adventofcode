#!/usr/bin/env python3


with open('input.txt') as file:
    offsets = [offset for offset in map(int, file.readlines())]

steps = 0
position = 0
while 0 <= position < len(offsets):
    steps += 1
    jump = offsets[position]
    offsets[position] = offsets[position] - 1 if offsets[position] >= 3 else offsets[position] + 1
    position += jump

print(steps)
