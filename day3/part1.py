#!/usr/bin/env python3


def get_ring_length(ring_number):
    return 4 * (ring_number * 2 - 1) + 4


def distance_from_ring_middle(spiral_length, rings, position):
    if rings == 0:
        return 0

    middle_number = spiral_length - rings
    distance = (middle_number - position) % (rings * 2)
    if distance > rings:
        distance = (rings * 2) - distance

    return distance


def get_distance_from_access_port(position):
    spiral_length = 1
    rings = 0
    while position > spiral_length:
        rings += 1
        spiral_length += get_ring_length(rings)

    return distance_from_ring_middle(spiral_length, rings, position) + rings


print(get_distance_from_access_port(289326))
