from collections import defaultdict
from typing import Dict, List, Set, Tuple


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    # Get antenna locations for each frequency.
    size = len(lines)
    all_locations: Dict[str, List[Tuple[int, int]]] = defaultdict(list)
    for row in range(size):
        for col in range(size):
            freq = lines[row][col]
            if freq != ".":
                all_locations[freq].append((row, col))

    # Calculate antinode locations for each pair of antennas of same frequency.
    antinodes: Set[Tuple[int, int]] = set()
    for locations in all_locations.values():
        for i1, (loc1_x, loc1_y) in enumerate(locations):
            for i2, (loc2_x, loc2_y) in enumerate(locations):
                if i1 != i2:
                    diff_x = loc2_x - loc1_x
                    diff_y = loc2_y - loc1_y

                    anti_x = loc2_x
                    anti_y = loc2_y
                    while 0 <= anti_x < size and 0 <= anti_y < size:
                        antinodes.add((anti_x, anti_y))
                        anti_x += diff_x
                        anti_y += diff_y

    print(len(antinodes))


solve("input-test.txt")  # 34
solve("input.txt")  # 1229
