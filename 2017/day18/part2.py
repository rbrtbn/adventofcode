#!/usr/bin/env python3
from collections import defaultdict


class Program(object):
    def __init__(self, program_id, snd_queue, rcv_queue):
        self.registers = defaultdict(int)
        self.registers['p'] = program_id
        self.snd_queue = snd_queue
        self.rcv_queue = rcv_queue
        self.position = 0
        self.snd_count = 0
        self.is_waiting = False
        self.is_terminated = False

    def _get_int_value(self, reg_or_val):
        try:
            return int(reg_or_val)
        except ValueError:
            return self.registers[reg_or_val]

    def run(self):
        while True:
            if self.position > len(instructions):
                self.is_terminated = True
                break

            position_change = 1
            if len(instructions[self.position]) == 2:
                inst, reg_or_val = instructions[self.position]
                if inst == 'snd':
                    val = self._get_int_value(reg_or_val)
                    self.snd_queue.append(val)
                    self.snd_count += 1
                elif inst == 'rcv':
                    if self.rcv_queue:
                        self.registers[reg_or_val] = self.rcv_queue.pop(0)
                        self.is_waiting = False
                    elif self.is_waiting:
                        self.is_terminated = True
                        break
                    else:
                        self.is_waiting = True
                        break
            else:
                inst, reg, val = instructions[self.position]
                val = self._get_int_value(val)
                if inst == 'set':
                    self.registers[reg] = val
                elif inst == 'add':
                    self.registers[reg] += val
                elif inst == 'mul':
                    self.registers[reg] *= val
                elif inst == 'mod':
                    self.registers[reg] %= val
                elif inst == 'jgz' and self._get_int_value(reg) > 0:
                    position_change = val

            self.position += position_change


instructions = []
with open('input.txt') as file:
    for line in file.readlines():
        instructions.append(tuple(line.split()))

queue_0 = []
queue_1 = []
program_0 = Program(0, queue_1, queue_0)
program_1 = Program(1, queue_0, queue_1)

while not program_0.is_terminated or not program_1.is_terminated:
    program_0.run()
    # print("run 0", "waiting" if program_0.is_waiting else "", "terminated" if program_0.is_terminated else "")
    # print(program_0.registers)
    program_1.run()
    # print("run 1", "waiting" if program_1.is_waiting else "", "terminated" if program_1.is_terminated else "")
    # print(program_1.registers)

print(program_1.snd_count)
