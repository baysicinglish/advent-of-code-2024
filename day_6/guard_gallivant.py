import itertools

OBSTACLE = "#"
VISITED = "X"
OCCUPIED = "^"

DIRECTIONS = itertools.cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])


def find_starting_position(patrol: list[list[str]]) -> list[int]:
    for row_num, row in enumerate(patrol):
        for column_num, space in enumerate(row):
            if space == "^":
                return [row_num, column_num]


def move(position, patrol, direction):
    patrol[position[0]][position[1]] = VISITED

    y = position[0] + direction[0]
    x = position[1] + direction[1]
    new_position = [y, x]

    if patrol[y][x] == OBSTACLE:
        direction = DIRECTIONS.__next__()
        new_position, direction = move(position, patrol, direction)

    patrol[new_position[0]][new_position[1]] = OCCUPIED

    return new_position, direction


if __name__ == "__main__":
    with open("day_6/inputs/input.txt") as patrol_route:
        patrol = [[space for space in row.strip()] for row in patrol_route]

    position = find_starting_position(patrol)
    direction = DIRECTIONS.__next__()

    while True:
        try:
            position, direction = move(position, patrol, direction)
            # print("\n".join(["".join([space for space in row]) for row in patrol]), end="\n\n")
        except IndexError:
            break

    print(sum([row.count("X") for row in patrol]))
