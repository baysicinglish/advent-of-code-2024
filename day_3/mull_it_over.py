import re


def scan_memory(line_of_memory: str) -> int:
    total = 0
    multiplication_commands = re.findall(r"mul\((\d+),(\d+)\)", line_of_memory)
    for command in multiplication_commands:
        total += int(command[0]) * int(command[1])

    return total


def remove_disabled_memory(line_of_memory: str) -> str:
    return re.sub(r"don't\(\).*?(do\(\)|$)", "<3", line_of_memory)


if __name__ == "__main__":
    with open("day_3/inputs/input.txt") as memory:
        corrupted_memory = memory.readlines()

    corrupted_memory = "<3".join([line.strip() for line in corrupted_memory])
    result = scan_memory(corrupted_memory)
    print(result)

    enabled_memory = remove_disabled_memory(corrupted_memory)
    result = scan_memory(enabled_memory)
    print(result)
