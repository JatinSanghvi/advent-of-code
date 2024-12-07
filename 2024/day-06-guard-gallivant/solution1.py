def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    # Get current position.
    pos = (-1, -1)
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == "^":
                pos = (row, col)
                break

    # Simulate guard's patrol route.
    size = len(lines)
    visited = set([pos])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    di = 0

    while True:
        new_pos = (pos[0] + directions[di][0], pos[1] + directions[di][1])
        if not (0 <= new_pos[0] < size and 0 <= new_pos[1] < size):
            break
        if lines[new_pos[0]][new_pos[1]] == "#":
            di = (di + 1) % 4
        else:
            pos = new_pos
            visited.add(pos)

    print(len(visited))


solve("input-test.txt")  # 41
solve("input.txt")  # 4826
