#!/usr/bin/env python3

##########################################################################
# This is a bad solution, but gave the right answer.                     #
# Right solution should use a 3 dimensional coordinate system, see here: #
# https://www.redblobgames.com/grids/hexagons/                           #
##########################################################################

with open('input.txt') as file:
    steps = file.readline().strip().split(',')

x = 0
y = 0
max_dist = 0
for step in steps:
    if step == 'n':
        y += 2
    elif step == 's':
        y -= 2
    elif step == 'ne':
        x += 1
        y += 1
    elif step == 'se':
        x += 1
        y -= 1
    elif step == 'nw':
        x -= 1
        y += 1
    elif step == 'sw':
        x -= 1
        y -= 1

    max_dist = max(max_dist, abs(x), abs(y))

print(max_dist)
