#!/usr/bin/env python3


def order_characters_alphabetically(word):
    return "".join(sorted(list(word)))


valid_phrase_count = 0
with open('input.txt') as file:
    for line in file.readlines():
        words = [order_characters_alphabetically(word) for word in line.strip().split()]
        if len(set(words)) == len(words):
            valid_phrase_count += 1

print(valid_phrase_count)
