def solve(path):
    with open(path) as file:
        line = file.readline()

    positions = sorted(int(pos) for pos in line.split(","))
    median = positions[len(positions) // 2 - 1]  # Works for even-sized arrays.
    fuel = sum(abs(pos - median) for pos in positions)
    print(fuel)


solve("input-test.txt")
solve("input.txt")
