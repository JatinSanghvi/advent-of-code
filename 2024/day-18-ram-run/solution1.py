from collections import deque
from typing import Set, Tuple


def solve(path: str, size: int, falls: int) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    blocks: Set[Tuple[int, int]] = set()
    for line in lines[:falls]:
        blocks.add(eval(line))

    visited: Set[Tuple[int, int]] = set()
    queue = deque([(0, (0, 0))])
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Find the distance to destination using breadth-first search.
    while True:
        dist, (x, y) = queue.popleft()
        if (x, y) == (size - 1, size - 1):
            break

        if (x, y) not in visited:
            visited.add((x, y))
            for mx, my in moves:
                x2, y2 = x + mx, y + my
                if 0 <= x2 < size and 0 <= y2 < size and (x2, y2) not in blocks:
                    queue.append((dist + 1, (x2, y2)))

    print(dist)


solve("input-test.txt", 7, 12)  # 22
solve("input.txt", 71, 1024)  # 290
