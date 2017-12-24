#!/usr/bin/env python3
import re

import math

from collections import defaultdict


class Coordinates(object):
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '<{x}, {y}, {z}>'.format(x=self.x, y=self.y, z=self.z)

    def get_length(self):
        return abs(self.x) + abs(self.y) + abs(self.z)


class Particle(object):
    def __init__(self, position: Coordinates, velocity: Coordinates, acceleration: Coordinates):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def __str__(self):
        return 'p={p}, v={v}, a={a}'.format(
            p=self.position,
            v=self.velocity,
            a=self.acceleration
        )

    def get_position(self, time):
        p, v, a = self.position, self.velocity, self.acceleration
        return Coordinates(
            p.x + v.x * time + (math.pow(time, 2) + time) / 2 * a.x,
            p.y + v.y * time + (math.pow(time, 2) + time) / 2 * a.y,
            p.z + v.z * time + (math.pow(time, 2) + time) / 2 * a.z,
        )


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

time = 0
while True:
    particles_at_pos = defaultdict(list)
    for index, particle in enumerate(particles):
        pos = particle.get_position(time)
        particles_at_pos[str(pos)].append(particle)

    if len(particles_at_pos) < len(particles):
        for parts in particles_at_pos.values():
            if len(parts) > 1:
                for part in parts:
                    particles.remove(part)

    print(len(particles))

    time += 1

