#!/usr/bin/env python3

checksum = 0
with open('input.txt') as file:
    for line in file.readlines():
        values = list(map(int, line.strip().split("\t")))
        checksum += max(values) - min(values)

print(checksum)
