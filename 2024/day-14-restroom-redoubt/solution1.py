import math
import re


def solve(path: str, width: int, height: int) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    quadrant = [0] * 4
    regex = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")

    for line in lines:
        match = regex.fullmatch(line)
        px, py, vx, vy = int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))  # type: ignore
        new_px, new_py = (px + 100 * vx) % width, (py + 100 * vy) % height

        # Ignore if robot is in the middle.
        if new_px == width // 2 or new_py == height // 2:
            continue

        # Add robot to its quadrant.
        quadrant[(new_px > width // 2) + 2 * (new_py > height // 2)] += 1

    print(math.prod(quadrant))


solve("input-test.txt", 11, 7)  # 12
solve("input.txt", 101, 103)  # 221616000
