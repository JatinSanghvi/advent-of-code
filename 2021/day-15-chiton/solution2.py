from queue import PriorityQueue


def solve(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file.readlines()]

    risks = [[int(char) for char in line] for line in lines]
    rows = len(risks)
    columns = len(risks[0])

    new_risks = []
    for row in range(5 * rows):
        new_risks_row = []
        for col in range(5 * columns):
            risk = risks[row % rows][col % columns]
            new_risks_row.append((risk + (row // rows) + (col // columns) - 1) % 9 + 1)
        new_risks.append(new_risks_row)

    risks = new_risks
    rows = len(risks)
    columns = len(risks[0])

    lowest_risks = PriorityQueue()
    lowest_risks.put((0, rows - 1, columns - 1))
    max_risk = 10 * (rows + columns)
    for row in range(rows):
        for col in range(columns):
            lowest_risks.put((max_risk, row, col))

    visited = set()

    while True:
        (min_risk, row, col) = lowest_risks.get()
        if (row, col) in visited: continue
        visited.add((row, col))

        if (row, col) == (0, 0):
            print(min_risk)
            return

        if row != 0: lowest_risks.put((risks[row][col] + min_risk, row - 1, col))
        if row != rows - 1: lowest_risks.put((risks[row][col] + min_risk, row + 1, col))
        if col != 0: lowest_risks.put((risks[row][col] + min_risk, row, col - 1))
        if col != columns - 1: lowest_risks.put((risks[row][col] + min_risk, row, col + 1))


solve("input-test.txt")
solve("input.txt")
