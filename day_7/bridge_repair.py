def parse_calibration(calibration):
    total, values = calibration.strip().split(":")
    total = int(total)
    values = [int(value) for value in values.split()]
    return total, values


def equation_is_possible(equation, current=0):
    target, numbers = equation
    if not numbers:
        return target - current == 0

    number, *numbers = numbers
    if not current:
        current = number
        return equation_is_possible((target, numbers), current=current)

    multiplied = current * number
    added = current + number

    if any([equation_is_possible((target, numbers), current=sum_) for sum_ in (multiplied, added) if sum_ <= target]):
        return True
    return False


if __name__ == "__main__":
    with open("day_7/inputs/input.txt") as calibrations:
        equations = [parse_calibration(calibration) for calibration in calibrations]

    print(sum([equation[0] for equation in equations if equation_is_possible(equation)]))
