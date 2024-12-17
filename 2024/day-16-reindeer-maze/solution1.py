from typing import Set, Tuple
import heapq


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    size = len(lines)
    sx, sy = next((x, y) for x in range(size) for y in range(size) if lines[x][y] == "S")  # Start tile.
    heap = [(0, (sx, sy, 0))]  # Priority queue indexed by points.
    visited: Set[Tuple[int, int, int]] = set()  # Visited tiles + directions.
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Visit all tiles + directions until we hit the end tile.
    while True:
        points, (x1, y1, d1) = heapq.heappop(heap)
        if lines[x1][y1] == "E":
            print(points)
            return
        if (x1, y1, d1) not in visited:
            visited.add((x1, y1, d1))
            x2, y2 = x1 + moves[d1][0], y1 + moves[d1][1]
            if lines[x2][y2] != "#":
                heapq.heappush(heap, (points + 1, (x2, y2, d1)))  # Move ahead.
            heapq.heappush(heap, (points + 1000, (x1, y1, (d1 - 1) % 4)))  # Turn left.
            heapq.heappush(heap, (points + 1000, (x1, y1, (d1 + 1) % 4)))  # Turn right.


solve("input-test-1.txt")  # 7036
solve("input-test-2.txt")  # 11048
solve("input.txt")  # 73404
