#!/usr/bin/env python3


with open('input.txt') as file:
    offsets = [offset for offset in map(int, file.readlines())]

steps = 0
position = 0
while 0 <= position < len(offsets):
    steps += 1
    offsets[position] += 1
    position += offsets[position] - 1

print(steps)
