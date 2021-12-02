#!/usr/bin/env python3

registers = {}
highest_value = 0
with open('input.txt') as file:
    for line in file.readlines():
        register, inc_dec, amount, _, condition_reg, condition_dir, condition_val = line.split()
        amount, condition_val = int(amount), int(condition_val)

        if register not in registers:
            registers[register] = 0
        if condition_reg not in registers:
            registers[condition_reg] = 0

        if (
            (condition_dir == '>' and registers[condition_reg] > condition_val) or
            (condition_dir == '<' and registers[condition_reg] < condition_val) or
            (condition_dir == '>=' and registers[condition_reg] >= condition_val) or
            (condition_dir == '<=' and registers[condition_reg] <= condition_val) or
            (condition_dir == '==' and registers[condition_reg] == condition_val) or
            (condition_dir == '!=' and registers[condition_reg] != condition_val)
        ):
            if inc_dec == 'inc':
                registers[register] += amount
                if registers[register] > highest_value:
                    highest_value = registers[register]
            else:
                registers[register] -= amount

print(max(registers.values()))
print(highest_value)
