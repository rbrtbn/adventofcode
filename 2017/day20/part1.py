#!/usr/bin/env python3
import re


class Coordinates(object):
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def get_length(self):
        return abs(self.x) + abs(self.y) + abs(self.z)


class Particle(object):
    def __init__(self, position: Coordinates, velocity: Coordinates, acceleration: Coordinates):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration


particles = []
with open('input.txt') as file:
    for line in file.readlines():
        matches = re.search('p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>', line)
        particle = Particle(
            Coordinates(int(matches[1]), int(matches[2]), int(matches[3])),
            Coordinates(int(matches[4]), int(matches[5]), int(matches[6])),
            Coordinates(int(matches[7]), int(matches[8]), int(matches[9])),
        )

        particles.append(particle)

acc_lengths = [particle.acceleration.get_length() for particle in particles]
print(acc_lengths.index(min(acc_lengths)))
