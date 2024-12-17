from collections import deque
from typing import Dict, Set, Tuple
import heapq


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    size = len(lines)
    points: Dict[Tuple[int, int, int], int] = {}  # Min points for each tile + direction.
    previous: Dict[Tuple[int, int, int], Set[Tuple[int, int, int]]] = {}  # Set of previous tiles + directions.

    sx, sy = next((x, y) for x in range(size) for y in range(size) if lines[x][y] == "S")  # Start tile.
    heap = [(0, (sx, sy, 0), (sx, sy, 0))]  # Priority queue indexed by points.
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Populate 'points' and 'previous' for each tile + direction in the map.
    while heap:
        pt, (x1, y1, d1), (x0, y0, d0) = heapq.heappop(heap)

        if (x1, y1, d1) not in points:  # New tile + direction.
            points[(x1, y1, d1)] = pt
            previous[(x1, y1, d1)] = set([(x0, y0, d0)])
            x2, y2 = x1 + moves[d1][0], y1 + moves[d1][1]
            if lines[x2][y2] != "#":
                heapq.heappush(heap, (pt + 1, (x2, y2, d1), (x1, y1, d1)))  # Move ahead.
            heapq.heappush(heap, (pt + 1000, (x1, y1, (d1 - 1) % 4), (x1, y1, d1)))  # Turn left.
            heapq.heappush(heap, (pt + 1000, (x1, y1, (d1 + 1) % 4), (x1, y1, d1)))  # Turn right.
        elif pt == points[(x1, y1, d1)]:  # Points same as existing tile + direction.
            previous[(x1, y1, d1)].add((x0, y0, d0))

    # Collect all directions at end tile that gets minimum points.
    ex, ey = next((x, y) for x in range(size) for y in range(size) if lines[x][y] == "E")  # End tile.
    min_pt = min(pt for (x, y, d), pt in points.items() if x == ex and y == ey)
    queue = deque((x, y, d) for (x, y, d), pt in points.items() if x == ex and y == ey and pt == min_pt)
    visited: Set[Tuple[int, int, int]] = set()

    # Backtrack and collect all previous tiles + directions in the minimum points path.
    while queue:
        xyd1 = queue.popleft()
        if xyd1 not in visited:
            visited.add(xyd1)
            for xyd2 in previous[xyd1]:
                queue.append(xyd2)

    # Collect tiles from tiles + directions.
    tiles = set((x, y) for x, y, d in visited)
    print(len(tiles))


solve("input-test-1.txt")  # 45
solve("input-test-2.txt")  # 64
solve("input.txt")  # 449
