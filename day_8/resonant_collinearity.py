import itertools

from collections import defaultdict


def subtract(node_a, node_b):
    return node_a[0] - node_b[0], node_a[1] - node_b[1]


def add(node_a, node_b):
    return node_a[0] + node_b[0], node_a[1] + node_b[1]


if __name__ == "__main__":
    with open("day_8/inputs/input.txt") as antenna_map:
        antenna_map = [row.strip() for row in antenna_map]

    antennas = defaultdict(list)
    for row_number, row in enumerate(antenna_map):
        for column_number, antenna in enumerate(row):
            if antenna != ".":
                antennas[antenna].append((row_number, column_number))

    antinodes = set()

    for locations in antennas.values():
        for pairing in itertools.combinations(locations, 2):
            difference = subtract(pairing[0], pairing[1])
            nodes = add(pairing[0], difference), subtract(pairing[1], difference)
            for node in nodes:
                if 0 <= node[0] < len(antenna_map) and 0 <= node[1] < len(antenna_map[0]):
                    antinodes.add(node)

    harmonic_antinodes = set()

    for locations in antennas.values():
        for pairing in itertools.combinations(locations, 2):
            difference = subtract(pairing[0], pairing[1])

            node = pairing[0]
            while 0 <= node[0] < len(antenna_map) and 0 <= node[1] < len(antenna_map[0]):
                harmonic_antinodes.add(node)
                node = subtract(node, difference)

            node = pairing[1]
            while 0 <= node[0] < len(antenna_map) and 0 <= node[1] < len(antenna_map[0]):
                harmonic_antinodes.add(node)
                node = add(node, difference)

    print(len(antinodes))
    print(len(harmonic_antinodes))
