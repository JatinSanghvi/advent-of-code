def solve(path):
    with open(path) as file:
        line = file.readline()

    positions = [int(pos) for pos in line.split(",")]

    min_fuel = pow(max(positions), 3)  # Sufficiently large number.
    for align_pos in range(min(positions), max(positions) + 1):
        fuel = sum(abs(pos - align_pos) * (abs(pos - align_pos) + 1) // 2 for pos in positions)
        min_fuel = min(min_fuel, fuel)

    print(min_fuel)


solve("input-test.txt")
solve("input.txt")
