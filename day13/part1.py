#!/usr/bin/env python3

firewall = {}
with open('input.txt') as file:
    for line in file.readlines():
        depth, layer_range = map(int, line.strip().split(':'))
        firewall[depth] = layer_range

severity = 0
scanner = 0
for position in range(max(firewall.keys())+1):
    if position in firewall and scanner % (firewall[position] * 2 - 2) == 0:
        severity += position * firewall[position]
    scanner += 1

print(severity)
