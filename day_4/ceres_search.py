TARGET = "XMAS"


def search_words(word_search, word) -> int:
    directions = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            directions.append((x, y))

    festivity_score = 0

    for row_number in range(len(word_search)):
        for column_number in range(len(word_search[0])):
            for direction in directions:
                is_xmas = True

                for letter_number, letter in enumerate(word):
                    x = row_number + (direction[0] * letter_number)
                    y = column_number + (direction[1] * letter_number)
                    if not (x in range(0, len(word_search)) and y in range(len(word_search[0])) and word_search[x][y] == letter):
                        is_xmas = False
                        break

                if is_xmas:
                    festivity_score += 1

    return festivity_score


def search_cross_mas(word_search) -> int:
    festivity_score = 0

    for row_number in range(1, len(word_search) - 1):
        for column_number in range(1, len(word_search[0]) - 1):
            if word_search[row_number][column_number] != "A":
                continue

            forward_slashy = word_search[row_number + 1][column_number - 1], word_search[row_number - 1][column_number + 1]
            backward_slashy = word_search[row_number - 1][column_number - 1], word_search[row_number + 1][column_number + 1]

            if frozenset(forward_slashy) == frozenset(backward_slashy) == frozenset(("M", "S")):
                festivity_score += 1

    return festivity_score


if __name__ == "__main__":
    with open("day_4/inputs/input.txt") as word_search:
        grid = [[letter for letter in row.strip()] for row in word_search]

    print(search_words(grid, TARGET))
    print(search_cross_mas(grid))
