import re

from typing import Dict, List


class Region:
    def __init__(self, face_row: int, face_col: int) -> None:
        self.face_row = face_row
        self.face_col = face_col


class Neighbor:
    def __init__(self, region: Region, dir: int) -> None:
        self.region = region
        self.dir = dir  # New direction if moved to this neighbor.


def solve(path: str, face_size: int, start_region: Region, neighbors: Dict[Region, List[Neighbor]]) -> None:
    # For each region, the neighbor-list will contain four neighbors, in order Left, Up, Right, and Down.

    with open(path) as file:
        lines = [line.rstrip('\n') for line in file.readlines()]

    map_ = [line for line in lines[:-2]]

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Left, Up, Right, Down.
    pattern = re.compile(r'L|R|\d+')
    path = lines[-1]

    row, col, dir, region = 0, 0, 0, start_region

    for step in pattern.findall(path):
        if step == 'L': dir = (dir - 1) % len(moves)
        elif step == 'R': dir = (dir + 1) % len(moves)
        else:
            for _ in range(int(step)):
                new_row, new_col, new_dir, new_region = row + moves[dir][0], col + moves[dir][1], dir, region

                if not 0 <= new_row < face_size or not 0 <= new_col < face_size:
                    new_dir = neighbors[region][dir].dir

                    if dir == 0:
                        if new_dir == 0: new_row, new_col = row, 0
                        elif new_dir == 1: new_row, new_col = 0, face_size - row - 1
                        elif new_dir == 2: new_row, new_col = face_size - row - 1, face_size - 1
                        elif new_dir == 3: new_row, new_col = face_size - 1, row
                    elif dir == 1:
                        if new_dir == 0: new_row, new_col = face_size - col - 1, 0
                        elif new_dir == 1: new_row, new_col = 0, col
                        elif new_dir == 2: new_row, new_col = col, face_size - 1
                        elif new_dir == 3: new_row, new_col = face_size - 1, face_size - col - 1
                    elif dir == 2:
                        if new_dir == 0: new_row, new_col = face_size - row - 1, 0
                        elif new_dir == 1: new_row, new_col = 0, row
                        elif new_dir == 2: new_row, new_col = row, face_size - 1
                        elif new_dir == 3: new_row, new_col = face_size - 1, face_size - row - 1
                    elif dir == 3:
                        if new_dir == 0: new_row, new_col = col, 0
                        elif new_dir == 1: new_row, new_col = 0, face_size - col - 1
                        elif new_dir == 2: new_row, new_col = face_size - col - 1, face_size - 1
                        elif new_dir == 3: new_row, new_col = face_size - 1, col

                    new_region = neighbors[region][dir].region

                if map_[new_region.face_row * face_size + new_row][new_region.face_col * face_size + new_col] == '#':
                    break
                else:
                    row, col, dir, region = new_row, new_col, new_dir, new_region

    print(1000 * (region.face_row * face_size + row + 1) + 4 * (region.face_col * face_size + col + 1) + dir)


def main():
    # ..0
    # 123
    # ..45

    regions = [Region(0, 2), Region(1, 0), Region(1, 1), Region(1, 2), Region(2, 2), Region(2, 3)]

    solve('input-test.txt', 4, regions[0], {
        regions[0]: [Neighbor(regions[5], 2), Neighbor(regions[3], 1), Neighbor(regions[2], 1), Neighbor(regions[1], 1)],
        regions[1]: [Neighbor(regions[2], 0), Neighbor(regions[4], 3), Neighbor(regions[5], 3), Neighbor(regions[0], 1)],
        regions[2]: [Neighbor(regions[3], 0), Neighbor(regions[4], 0), Neighbor(regions[1], 2), Neighbor(regions[0], 0)],
        regions[3]: [Neighbor(regions[5], 1), Neighbor(regions[4], 1), Neighbor(regions[2], 2), Neighbor(regions[0], 3)],
        regions[4]: [Neighbor(regions[5], 0), Neighbor(regions[1], 3), Neighbor(regions[2], 3), Neighbor(regions[3], 3)],
        regions[5]: [Neighbor(regions[0], 2), Neighbor(regions[1], 0), Neighbor(regions[4], 2), Neighbor(regions[3], 2)],
    })  # 5031

    # .01
    # .2
    # 34
    # 5

    regions = [Region(0, 1), Region(0, 2), Region(1, 1), Region(2, 0), Region(2, 1), Region(3, 0)]

    solve('input.txt', 50, regions[0], {
        regions[0]: [Neighbor(regions[1], 0), Neighbor(regions[2], 1), Neighbor(regions[3], 0), Neighbor(regions[5], 0)],
        regions[1]: [Neighbor(regions[4], 2), Neighbor(regions[2], 2), Neighbor(regions[0], 2), Neighbor(regions[5], 3)],
        regions[2]: [Neighbor(regions[1], 3), Neighbor(regions[4], 1), Neighbor(regions[3], 1), Neighbor(regions[0], 3)],
        regions[3]: [Neighbor(regions[4], 0), Neighbor(regions[5], 1), Neighbor(regions[0], 0), Neighbor(regions[2], 0)],
        regions[4]: [Neighbor(regions[1], 2), Neighbor(regions[5], 2), Neighbor(regions[3], 2), Neighbor(regions[2], 3)],
        regions[5]: [Neighbor(regions[4], 3), Neighbor(regions[1], 1), Neighbor(regions[0], 1), Neighbor(regions[3], 3)],
    })  # 104385


if __name__ == '__main__':
    main()
