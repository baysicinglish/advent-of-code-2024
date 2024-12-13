
def trace_borders(regional_plant, position):
    total_area = 0
    total_edges = 0

    if 0 <= position[0] < len(GARDEN) and 0 <= position[1] < len(GARDEN[0]):
        plant = GARDEN[position[0]][position[1]]

        if plant == regional_plant:
            if position in SEEN:
                return total_area, total_edges

            total_area += 1
            SEEN.add(position)

            for direction in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                area, edges = trace_borders(regional_plant, (position[0] + direction[0], position[1] + direction[1]))
                total_area += area
                total_edges += edges

            return total_area, total_edges

    return total_area, total_edges + 1


if __name__ == "__main__":
    with open("day_12/inputs/input.txt") as garden_map:
        GARDEN = [[plant for plant in row.strip()] for row in garden_map]

    SEEN = set()
    fence_price = 0

    for row_number, row in enumerate(GARDEN):
        for column_number, plant in enumerate(row):
            if (row_number, column_number) in SEEN:
                continue

            region_area, region_edges = trace_borders(plant, (row_number, column_number))
            fence_price += region_area * region_edges

    print(fence_price)
