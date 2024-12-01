def get_ids_by_group(location_ids: list[list[str]]):
    group_one_ids = sorted([int(ids[0]) for ids in location_ids])
    group_two_ids = sorted([int(ids[1]) for ids in location_ids])

    return group_one_ids, group_two_ids


def solve_part_one(group_one_ids: list[int], group_two_ids: list[int]):
    total_distance = 0
    for location in range(len(location_ids)):
        total_distance += abs(group_two_ids[location] - group_one_ids[location])

    return total_distance


def solve_part_two(group_one_ids: list[int], group_two_ids: list[int]):
    similarity_score = 0
    for location_id in group_one_ids:
        similarity_score += location_id * group_two_ids.count(location_id)

    return similarity_score


if __name__ == "__main__":
    with open("day_1/inputs/input.txt") as file:
        location_ids = [line.split() for line in file]
        group_one_ids, group_two_ids = get_ids_by_group(location_ids)

        print(solve_part_one(group_one_ids, group_two_ids))
        print(solve_part_two(group_one_ids, group_two_ids))
