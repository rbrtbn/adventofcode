#!/usr/bin/env python3
import re


programs = []
subprograms = []
with open('input.txt') as file:
    for line in file.readlines():
        m = re.search('(\w+) \((\d+)\)( -> (.*))?', line)
        programs.append(m.group(1))
        subprograms += m.group(4).split(', ') if m.group(4) is not None else []

print((set(programs) - set(subprograms)).pop())
