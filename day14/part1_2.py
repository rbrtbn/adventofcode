#!/usr/bin/env python2


def knot_hash(input_string):
    lengths = list(map(ord, input_string))

    lengths += [17, 31, 73, 47, 23]

    marks = 256
    numbers = range(marks)
    current_position = 0
    skip_size = 0

    for _ in range(64):
        for length in lengths:
            end_position = current_position + length
            if end_position > len(numbers):
                reversed_numbers = numbers[current_position:len(numbers)] + numbers[:end_position - len(numbers)]
                reversed_numbers = reversed_numbers[::-1]
                numbers[current_position:len(numbers)] = reversed_numbers[:len(numbers) - current_position]
                numbers[:end_position - len(numbers)] = reversed_numbers[len(numbers) - current_position:]
            else:
                numbers[current_position:end_position] = numbers[current_position:end_position][::-1]

            current_position = (end_position + skip_size) % marks
            skip_size += 1

    dense_hash = []
    for start in range(0, 256, 16):
        hashed_value = numbers[start]
        for index in range(start + 1, start + 16):
            hashed_value ^= numbers[index]
        dense_hash.append(hashed_value)

    def knot_hash_inner(num):
        return str(hex(num))[2:].zfill(2)

    return "".join(map(knot_hash_inner, dense_hash))


key_string = 'jxqlasbh'
# key_string = 'flqrgnkx'

used = 0
grid = []
for row in range(128):
    row_hash = knot_hash('{}-{}'.format(key_string, row))
    grid_row = []
    for hex_digit in row_hash:
        grid_row += list(map(int, bin(int(hex_digit, 16))[2:].zfill(4)))

    used += grid_row.count(1)
    grid.append(grid_row)

print(used)


def get_connected_region(row, col, known_region=None):
    if known_region is None:
        known_region = set()

    known_region.add((row, col))
    if col > 0 and grid[row][col - 1] == 1 and (row, col - 1) not in known_region:
        known_region.update(get_connected_region(row, col - 1, known_region))
    if row > 0 and grid[row - 1][col] == 1 and (row - 1, col) not in known_region:
        known_region.update(get_connected_region(row - 1, col, known_region))
    if col < 127 and grid[row][col + 1] == 1 and (row, col + 1) not in known_region:
        known_region.update(get_connected_region(row, col + 1, known_region))
    if row < 127 and grid[row + 1][col] == 1 and (row + 1, col) not in known_region:
        known_region.update(get_connected_region(row + 1, col, known_region))

    return known_region


region_count = 0
region_grid = [[-1 for _ in range(128)] for _ in range(128)]
for row in range(128):
    for col in range(128):
        if region_grid[row][col] == -1:
            if grid[row][col] == 0:
                region_grid[row][col] = 0
            else:
                region = get_connected_region(row, col)
                region_count += 1
                for row2, col2 in region:
                    region_grid[row2][col2] = region_count

print(region_count)
