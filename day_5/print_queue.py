from collections import defaultdict

if __name__ == "__main__":
    with open("day_5/inputs/input.txt") as print_instructions:
        prerequisites = defaultdict(set)
        for line in print_instructions:
            if not (prerequisite := line.strip()):
                break

            after, before = prerequisite.split("|")
            prerequisites[before].add(int(after))

        updates = [[int(page) for page in update.strip().split(",")] for update in print_instructions]

    middle_page_sum = 0

    for update in updates:
        midpoint = len(update) // 2
        middle_page_sum += update[midpoint]
        too_late = set()

        for page in update:
            if page in too_late:
                middle_page_sum -= update[midpoint]
                break

            too_late = too_late.union(prerequisites[str(page)])

    print(middle_page_sum)

