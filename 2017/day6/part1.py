#!/usr/bin/env python3


def get_state(memory_banks):
    return ",".join(map(str, memory_banks))


previous_states = set()
with open('input.txt') as file:
    memory_banks = list(map(int, file.readline().strip().split("\t")))
    cycles = 0
    while get_state(memory_banks) not in previous_states:
        previous_states.add(get_state(memory_banks))
        most_blocks = max(memory_banks)
        most_blocks_pos = memory_banks.index(most_blocks)
        memory_banks[most_blocks_pos] = 0
        for pos in range(most_blocks_pos + 1, most_blocks_pos + most_blocks + 1):
            memory_banks[pos % len(memory_banks)] += 1
        cycles += 1

print(cycles)
