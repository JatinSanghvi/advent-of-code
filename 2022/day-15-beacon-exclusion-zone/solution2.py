import re

from collections import defaultdict
from typing import Dict, List, Tuple


def solve(path, max_xy):
    with open(path) as file:
        lines = [line.rstrip('\n') for line in file.readlines() if line]

    coverages: List[Tuple[int, int, int]] = []
    for line in lines:
        match = re.match(r'^Sensor at x=(\-?\d+), y=(\-?\d+): closest beacon is at x=(\-?\d+), y=(\-?\d+)$', line)
        sx, sy, bx, by = map(int, [match[1], match[2], match[3], match[4]])
        dist_xy = abs(sx - bx) + abs(sy - by)
        coverages.append((sx, sy, dist_xy))

    # Store positions of all borders.
    borders: Dict[Tuple[int, int], int] = defaultdict(int)
    for sx, sy, dist_xy in coverages:
        dist_xy += 1
        for x in range(max(0, sx - dist_xy), min(max_xy, sx + dist_xy) + 1):
            dist_y = dist_xy - abs(sx - x)
            if 0 <= sy - dist_y <= max_xy: borders[x, sy - dist_y] += 1
            if 0 <= sy + dist_y <= max_xy: borders[x, sy + dist_y] += 1

    # Since there's only one possible position, the beacon should lie on the outer-border of sensors' coverage areas.
    # All four of its diagonally opposite positions should be covered by different sensors, hence there should be at
    # least 4 borders overlapping at this position, unless this position is at the edge or corner of the search area.

    positions: List[Tuple[int, int]] = []
    for (x, y), count in borders.items():
        if (x in [0, max_xy] and y in [0, max_xy] and count >= 1) or \
        (x in [0, max_xy] or y in [0, max_xy] and count >= 2) or \
        count >= 4:
            positions.append((x, y))

    # Filter out positions that fall under the coverage areas of sensors.
    for x, y in positions:
        for sx, sy, dist_xy in coverages:
            if abs(sx - x) + abs(sy - y) <= dist_xy:
                break
        else:
            print(4000000 * x + y)
            return


def main():
    solve('input-test.txt', 20)  # 56000011
    solve('input.txt', 4000000)  # 11645454855041


if __name__ == '__main__':
    main()
