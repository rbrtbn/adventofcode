#!/usr/bin/env python3
import re


programs = {}
with open('input.txt') as file:
    for line in file.readlines():
        m = re.search('(\w+) \((\d+)\)( -> (.*))?', line)
        program = m.group(1)
        weight = m.group(2)
        subprograms = m.group(4).split(', ') if m.group(4) is not None else []

        programs[program] = {
            'weight': weight,
            'subprograms': subprograms
        }


def calculate_total_weight(program):
    if 'total_weight' not in programs[program]:
        total_weight = int(programs[program]['weight'])
        for subprogram in programs[program]['subprograms']:
            total_weight += calculate_total_weight(subprogram)
        programs[program]['total_weight'] = total_weight

    return programs[program]['total_weight']


for program, info in programs.items():
    sub_weights = []
    for subprogram in info['subprograms']:
        sub_weights.append(calculate_total_weight(subprogram))

    if len(set(sub_weights)) > 1:
        print(program, info, sub_weights)

# such...
print(programs['fabacam'])
