from typing import Deque, Tuple
from collections import deque


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    rows = len(lines)
    cols = len(lines[0])
    neighbors = [[0] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == "@":
                for ir, ic in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    if -1 < (r + ir) < rows and -1 < (c + ic) < cols and lines[r + ir][c + ic] == "@":
                        neighbors[r + ir][c + ic] += 1

    accessible: Deque[Tuple[int, int]] = deque()
    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == "@" and neighbors[r][c] < 4:
                accessible.append((r, c))

    removable = 0
    while accessible:
        removable += 1
        (r, c) = accessible.popleft()
        for ir, ic in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            if -1 < (r + ir) < rows and -1 < (c + ic) < cols and lines[r + ir][c + ic] == "@":
                neighbors[r + ir][c + ic] -= 1
                if neighbors[r + ir][c + ic] == 3:
                    accessible.append((r + ir, c + ic))

    print(removable)


solve("input-test.txt")  # 43
solve("input.txt")  # 8665
