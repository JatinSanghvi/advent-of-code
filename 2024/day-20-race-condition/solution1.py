from collections import deque
from typing import Dict, Tuple


def solve(path: str, saves: int) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    size = len(lines)
    ex, ey = next((x, y) for x in range(size) for y in range(size) if lines[x][y] == "E")
    queue = deque([((ex, ey), 0)])
    distances: Dict[Tuple[int, int], int] = {}
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Find the distances of all points from the end.
    while queue:
        (x, y), dist = queue.popleft()
        if (x, y) not in distances:
            distances[(x, y)] = dist
            for mx, my in moves:
                x2, y2 = x + mx, y + my
                if lines[x2][y2] != "#":
                    queue.append(((x2, y2), dist + 1))

    cheats = 0
    neighbors = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-2, 0), (2, 0), (0, -2), (0, 2)]

    # Find all combination of coordinates with distance 2 and saving >= 'saves' picoseconds.
    for x in range(size):
        for y in range(size):
            if (x, y) in distances:
                dist = distances[(x, y)]
                for nx, ny in neighbors:
                    x2, y2 = x + nx, y + ny
                    if (x2, y2) in distances and distances[(x2, y2)] - dist - 2 >= saves:
                        cheats += 1

    print(cheats)


solve("input-test.txt", 64)  # 1
solve("input-test.txt", 2)  # 44
solve("input.txt", 100)  # 1406
