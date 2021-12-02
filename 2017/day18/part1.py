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
sound_freq = 0
while True:
    if position > len(instructions):
        break

    if len(instructions[position]) == 2:
        inst, val = instructions[position]
        reg = None
    else:
        inst, reg, val = instructions[position]

    val = get_int_value(val)

    position_change = 1
    if reg is None:
        if inst == 'snd':
            sound_freq = val
        elif inst == 'rcv' and val != 0:
            print(sound_freq)
            break
    else:
        if inst == 'set':
            registers[reg] = val
        elif inst == 'add':
            registers[reg] += val
        elif inst == 'mul':
            registers[reg] *= val
        elif inst == 'mod':
            registers[reg] %= val
        elif inst == 'jgz' and get_int_value(reg) > 0:
            position_change = val

    position += position_change



