import re


def scan_memory(line_of_memory: str) -> int:
    total = 0
    multiplication_commands = re.findall(r"mul\((\d+),(\d+)\)", line_of_memory)
    for command in multiplication_commands:
        total += int(command[0]) * int(command[1])

    return total


if __name__ == "__main__":
    with open("day_3/inputs/input.txt") as corrupted_memory:
        result = sum([scan_memory(line) for line in corrupted_memory])
        print(result)
