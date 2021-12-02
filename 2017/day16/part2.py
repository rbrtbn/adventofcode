#!/usr/bin/env python3

programs = list('abcdefghijklmnop')

program_states = []


def swap(pos_a, pos_b):
    program_at_a = programs[pos_a]
    programs[pos_a] = programs[pos_b]
    programs[pos_b] = program_at_a


with open('input.txt') as file:
    dance_moves = file.readline().strip().split(',')

iterations = 1000000000
for _ in range(iterations):
    for dance_move in dance_moves:
        if dance_move[0] == 's':
            count = int(dance_move[1:])
            programs = programs[-count:] + programs[:-count]
        elif dance_move[0] == 'x':
            pos_a, pos_b = map(int, dance_move[1:].split('/'))
            swap(pos_a, pos_b)
        elif dance_move[0] == 'p':
            prog_a, prog_b = dance_move[1:].split('/')
            swap(programs.index(prog_a), programs.index(prog_b))

    program_state = ''.join(programs)
    if program_state not in program_states:
        program_states.append(program_state)
    else:
        no_of_states = len(program_states)
        last_state = program_states[(iterations - 1) % len(program_states)]
        print(last_state)
        break
