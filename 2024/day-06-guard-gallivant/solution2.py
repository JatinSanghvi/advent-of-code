def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    size = len(lines)
    grid = [list(line) for line in lines]

    # Get start position.
    start_row, start_col = -1, -1
    for row in range(size):
        for col in range(size):
            if grid[row][col] == "^":
                start_row, start_col = row, col
                break

    # Simulate guard's patrol route with obstacle in each position.
    obstructions = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for obs_row in range(size):
        for obs_col in range(size):
            if grid[obs_row][obs_col] == ".":
                grid[obs_row][obs_col] = "#"

                row, col, dir_ = start_row, start_col, 0
                positions = set([(row, col, dir_)])

                while True:
                    new_row, new_col = row + directions[dir_][0], col + directions[dir_][1]

                    if not (0 <= new_row < size and 0 <= new_col < size):
                        break
                    elif grid[new_row][new_col] == "#":
                        dir_ = (dir_ + 1) % 4
                    else:
                        row, col = new_row, new_col

                    if (row, col, dir_) in positions:
                        obstructions += 1
                        break

                    positions.add((row, col, dir_))

                grid[obs_row][obs_col] = "."

    print(obstructions)


solve("input-test.txt")  # 6
solve("input.txt")  # 1721
