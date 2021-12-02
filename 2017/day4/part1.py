#!/usr/bin/env python3

valid_phrase_count = 0
with open('input.txt') as file:
    for line in file.readlines():
        words = line.strip().split()
        if len(set(words)) == len(words):
            valid_phrase_count += 1

print(valid_phrase_count)
