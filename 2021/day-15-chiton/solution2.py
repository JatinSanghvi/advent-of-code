def solve(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file.readlines()]

    risks = [[int(char) for char in line] for line in lines]
    rows = len(risks)
    columns = len(risks[0])

    new_risks = []
    for row in range(5):
        for risks_row in risks:
            new_risks_row = []
            for col in range(5):
                new_risks_row += [(risk + row + col - 1) % 9 + 1 for risk in risks_row]
            new_risks.append(new_risks_row)

    risks = new_risks
    rows = len(risks)
    columns = len(risks[0])

    lowest_risks = [[10 * (rows + columns)] * columns for _ in range(rows)]
    lowest_risks[rows - 1][columns - 1] = 0

    changed = True
    while changed:
        changed = False
        for row in reversed(range(rows)):
            for col in reversed(range(columns)):
                min_risk = lowest_risks[row][col]
                if row != 0: min_risk = min(min_risk, risks[row - 1][col] + lowest_risks[row - 1][col])
                if row != rows - 1: min_risk = min(min_risk, risks[row + 1][col] + lowest_risks[row + 1][col])
                if col != 0: min_risk = min(min_risk, risks[row][col - 1] + lowest_risks[row][col - 1])
                if col != columns - 1: min_risk = min(min_risk, risks[row][col + 1] + lowest_risks[row][col + 1])

                if lowest_risks[row][col] != min_risk:
                    lowest_risks[row][col] = min_risk
                    changed = True

    print(lowest_risks[0][0])


solve("input-test.txt")
solve("input.txt")
