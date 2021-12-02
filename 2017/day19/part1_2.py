#!/usr/bin/env python3
from collections import namedtuple
from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


Position = namedtuple('Position', ['x', 'y'])


class Map(object):
    def __init__(self):
        self.map = []
        with open('input.txt') as file:
            for line in file.readlines():
                self.map.append(list(line.strip("\n")))

    def _is_on_map(self, pos: Position):
        if 0 <= pos.x < len(self.map):
            if 0 <= pos.y < len(self.map[pos.x]):
                return True

        return False

    def _is_on_path(self, pos: Position):
        return self.map[pos.x][pos.y] != ' '

    def get_possible_directions(self, pos: Position):
        directions = {
            Direction.UP: Position(pos.x - 1, pos.y),
            Direction.DOWN: Position(pos.x + 1, pos.y),
            Direction.LEFT: Position(pos.x, pos.y - 1),
            Direction.RIGHT: Position(pos.x, pos.y + 1),
        }

        ret = []
        if self._is_on_map(pos):
            for dir, dir_pos in directions.items():
                if self._is_on_map(dir_pos) and self._is_on_path(dir_pos):
                    ret.append(dir)

        return ret


my_map = Map()

preferred_directions = {
    Direction.UP: [Direction.UP, Direction.LEFT, Direction.RIGHT],
    Direction.DOWN: [Direction.DOWN, Direction.LEFT, Direction.RIGHT],
    Direction.LEFT: [Direction.LEFT, Direction.UP, Direction.DOWN],
    Direction.RIGHT: [Direction.RIGHT, Direction.UP, Direction.DOWN],
}

position = Position(0, my_map.map[0].index('|'))
last_direction = Direction.DOWN
letters = []
path = []
while True:
    path.append(my_map.map[position.x][position.y])
    if my_map.map[position.x][position.y] not in [' ', '|', '-', '+']:
        letters.append(my_map.map[position.x][position.y])

    possible_directions = my_map.get_possible_directions(position)
    direction = None
    for preferred_direction in preferred_directions[last_direction]:
        if preferred_direction in possible_directions:
            direction = preferred_direction
            break

    if direction == Direction.UP:
        position = Position(position.x - 1, position.y)
    elif direction == Direction.DOWN:
        position = Position(position.x + 1, position.y)
    elif direction == Direction.LEFT:
        position = Position(position.x, position.y - 1)
    elif direction == Direction.RIGHT:
        position = Position(position.x, position.y + 1)
    else:
        break

    last_direction = direction
    # print(last_direction, position)

# print(path)
print(len(path))
print("".join(letters))
