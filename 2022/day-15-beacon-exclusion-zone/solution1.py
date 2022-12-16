import re

from typing import List, Tuple


def solve(path, y):
    with open(path) as file:
        lines = [line.rstrip('\n') for line in file.readlines() if line]

    coverages: List[Tuple[int, int]] = []
    beacons: List[int] = []

    for line in lines:
        match = re.match(r'^Sensor at x=(\-?\d+), y=(\-?\d+): closest beacon is at x=(\-?\d+), y=(\-?\d+)$', line)
        sx, sy, bx, by = map(int, [match[1], match[2], match[3], match[4]])

        # dist == abs(sx - bx) + abs(sy - by) == abs(sx - xmin/xmax) + abs(sy - y)
        dist_x = abs(sx - bx) + abs(sy - by) - abs(sy - y)
        if dist_x >= 0:
            coverages.append((sx - dist_x, sx + dist_x))

        if by == y:
            beacons.append(bx)

    min_x = min(cov[0] for cov in coverages)
    max_x = max(cov[1] for cov in coverages)

    row = ['.'] * (max_x - min_x + 1)
    for cov in coverages:
        for x in range(cov[0], cov[1] + 1):
            row[x - min_x] = '#'

    for x in beacons:
        row[x - min_x] = 'B'

    print(sum(x == '#' for x in row))


def main():
    solve('input-test.txt', 10)  # 26
    solve('input.txt', 2000000)  # 4876693


if __name__ == '__main__':
    main()
