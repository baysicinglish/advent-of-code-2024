MEMO = {}


def calculate_stones(stones, blinks):
    if not blinks:
        return len(stones)

    stone_counts = []
    for stone in stones:
        if seen := MEMO.get((stone, blinks)):
            stone_counts.append(seen)
        else:
            stone_count = calculate_stones(blink(stone), blinks - 1)
            MEMO[(stone, blinks)] = stone_count
            stone_counts.append(stone_count)

    return sum(stone_counts)


def blink(stone):
    if stone == 0:
        return [1]

    stone_digits = str(stone)
    if not (length := len(stone_digits)) % 2:
        split = [int(stone_digits[:length // 2]), int(stone_digits[length // 2:])]
        return split

    return [stone * 2024]


if __name__ == "__main__":
    with open("day_11/inputs/input.txt") as starting_arrangement:
        stones = [int(stone) for stone in starting_arrangement.readline().strip().split()]

    print(calculate_stones(stones, 25))
    print(calculate_stones(stones, 75))
