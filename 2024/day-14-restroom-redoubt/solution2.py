from typing import List, Set, Tuple
import re


def solve(path: str, width: int, height: int) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    regex = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")
    positions: List[Tuple[int, int]] = []
    velocities: List[Tuple[int, int]] = []

    for line in lines:
        match = regex.fullmatch(line)
        positions.append((int(match.group(1)), int(match.group(2))))  # type: ignore
        velocities.append((int(match.group(3)), int(match.group(4))))  # type: ignore

    # Look for the time when no robot position overlaps.
    for seconds in range(10000):
        new_positions: Set[Tuple[int, int]] = set()
        for (px, py), (vx, vy) in zip(positions, velocities):
            new_px, new_py = (px + seconds * vx) % width, (py + seconds * vy) % height
            if (new_px, new_py) in new_positions:
                break
            new_positions.add((new_px, new_py))
        else:
            for row in range(height):
                print("".join("." if (row, col) in new_positions else "*" for col in range(width)))
            print(seconds)
            break


solve("input.txt", 101, 103)  # 7572
