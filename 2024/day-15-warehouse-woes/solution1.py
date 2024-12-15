from typing import List


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    size = lines.index("")
    warehouse: List[List[str]] = [list(line) for line in lines[:size]]
    moves = "".join(lines[size + 1 :])
    displacement = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

    # Robot's initial position.
    x, y = next((x, y) for x in range(size) for y in range(size) if warehouse[x][y] == "@")
    for move in moves:
        dx, dy = displacement[move]

        # Find length of boxes (including the robot) to be moved.
        box_len = 1
        while (item := warehouse[x + box_len * dx][y + box_len * dy]) not in ("#", "."):
            box_len += 1

        # If the other end of boxes is an empty space, then move the boxes and robot.
        if item == ".":
            while box_len > 0:
                warehouse[x + box_len * dx][y + box_len * dy] = warehouse[x + (box_len - 1) * dx][y + (box_len - 1) * dy]
                box_len -= 1

            warehouse[x][y] = "."
            x, y = x + dx, y + dy

    gps_sum = sum(100 * x + y for x in range(size) for y in range(size) if warehouse[x][y] == "O")
    print(gps_sum)


solve("input-test-1.txt")  # 2028
solve("input-test-2.txt")  # 10092
solve("input.txt")  # 1538871
