#!/usr/bin/env python3
from collections import defaultdict

registers = defaultdict(int)
instructions = []
with open('input.txt') as file:
    for line in file.readlines():
        instructions.append(tuple(line.split()))


def get_int_value(reg_or_val):
    try:
        return int(reg_or_val)
    except ValueError:
        return registers[reg_or_val]


position = 0
mul_called = 0
while True:
    if not (0 <= position < len(instructions)):
        break

    inst, reg, val = instructions[position]
    val = get_int_value(val)

    position_change = 1
    if inst == 'set':
        registers[reg] = val
    elif inst == 'sub':
        registers[reg] -= val
    elif inst == 'mul':
        registers[reg] *= val
        mul_called += 1
    elif inst == 'jnz' and get_int_value(reg) != 0:
        position_change = val

    position += position_change

print(mul_called)
