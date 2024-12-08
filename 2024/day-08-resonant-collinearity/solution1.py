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

    # Calculate antinode location for each pair of antennas of same frequency.
    antinodes: Set[Tuple[int, int]] = set()
    for locations in all_locations.values():
        for i1, (loc1_x, loc1_y) in enumerate(locations):
            for i2, (loc2_x, loc2_y) in enumerate(locations):
                if i1 != i2:
                    anti_x = 2 * loc1_x - loc2_x
                    anti_y = 2 * loc1_y - loc2_y
                    if 0 <= anti_x < size and 0 <= anti_y < size:
                        antinodes.add((anti_x, anti_y))

    print(len(antinodes))


solve("input-test.txt")  # 14
solve("input.txt")  # 371
