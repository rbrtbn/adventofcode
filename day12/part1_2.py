#!/usr/bin/env python3
import re

from collections import defaultdict

pipes = defaultdict(set)
with open('input.txt') as file:
    for line in file.readlines():
        m = re.search('(\d+) <-> (.*)', line.strip())
        source = int(m.group(1))
        targets = list(map(int, m.group(2).split(",")))

        pipes[source].update(targets)
        for target in targets:
            pipes[target].add(source)

groups = []
all_banks = set(pipes.keys())
while len(all_banks):
    group_source = all_banks.pop()
    connected = set(pipes[group_source])
    visited = {group_source}
    while len(connected):
        el = connected.pop()
        if el in visited:
            continue

        connected.update(pipes[el])
        visited.add(el)
        all_banks.remove(el)

    groups.append(visited)
    if 0 in visited:
        print("connected to 0:", len(visited))

print("groups:", len(groups))
