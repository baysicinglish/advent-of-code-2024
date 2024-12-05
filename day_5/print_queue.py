from collections import defaultdict


def get_updates_and_prerequisites(print_instructions):
    prerequisites = defaultdict(set)
    for line in print_instructions:
        if not (prerequisite := line.strip()):
            break

        after, before = prerequisite.split("|")
        prerequisites[before].add(int(after))

    updates = [[int(page) for page in update.strip().split(",")] for update in print_instructions]
    return updates, prerequisites


def is_in_order(update, prerequisites):
    too_late = set()

    for page in update:
        if page in too_late:
            return False

        too_late = too_late.union(prerequisites[str(page)])

    return True


if __name__ == "__main__":
    with open("day_5/inputs/input.txt") as print_instructions:
        updates, prerequisites = get_updates_and_prerequisites(print_instructions)

    middle_page_of_ordered_updates = [
        update[len(update) // 2] for update in updates if is_in_order(update, prerequisites)
    ]
    print(sum(middle_page_of_ordered_updates))
