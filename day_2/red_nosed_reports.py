def report_is_safe(report: list[int]):
    previous = report[0]
    is_increasing = (report[1] - report[0]) > 0

    for level in report[1:]:
        change = level - previous

        is_gradual = 1 <= abs(change) <= 3
        is_consistent = change > 0 if is_increasing else change < 0

        if not (is_gradual and is_consistent):
            return False

        previous = level

    return True


def report_is_almost_safe(report: list[int]):
    if report_is_safe(report):
        return True

    for level_index in range(len(report)):
        if report_is_safe(report[:level_index] + report[level_index + 1:]):
            return True

    return False


if __name__ == "__main__":
    with open("day_2/inputs/input.txt") as unusual_data:
        unusual_data = [[int(level) for level in report.split()] for report in unusual_data]

        safe_reports = [report for report in unusual_data if report_is_safe(report)]
        print(len(safe_reports))

        safe_reports = [report for report in unusual_data if report_is_almost_safe(report)]
        print(len(safe_reports))
