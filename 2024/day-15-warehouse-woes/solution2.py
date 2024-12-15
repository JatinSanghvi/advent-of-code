from typing import Dict, List, Tuple


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    size = lines.index("")

    # Transform original map to double-width map.
    transform = {"#": "##", "O": "[]", ".": "..", "@": "@."}
    warehouse: List[List[str]] = [[transform[char][i] for char in line for i in (0, 1)] for line in lines[:size]]

    moves = "".join(lines[size + 1 :])
    displacement = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

    # Robot's initial position.
    rx, ry = next((x, y) for x in range(size) for y in range(2 * size) if warehouse[x][y] == "@")
    for move in moves:
        dx, dy = displacement[move]
        all_updates = {(rx, ry): "."}  # Updates to the map if the robot and boxes can be moved.

        dist = 1
        dist_updates = {(rx + dx, ry + dy): "@"}  # Updates at particular distance 'dist'.
        all_updates.update(dist_updates)

        while True:
            # Find updates at higher and higher distances with every iteration.
            dist1_updates: Dict[Tuple[int, int], str] = {}

            any_wall = False  # Any new position has a wall.
            all_spaces = True  # All new positions have spaces.

            for x, y in dist_updates:
                if warehouse[x][y] == "#":
                    any_wall = True
                elif warehouse[x][y] != ".":
                    all_spaces = False
                    if dy != 0:  # Horizonal movement (simple case).
                        dist1_updates[(x, y + dy)] = warehouse[x][y]
                    elif warehouse[x][y] == "[":  # Vertical movement encountered '['.
                        dist1_updates.update({(x + dx, y): "[", (x + dx, y + 1): "]"})
                        if (x, y + 1) not in all_updates:
                            all_updates[(x, y + 1)] = "."
                    elif warehouse[x][y] == "]":  # Vertical movement encountered ']'.
                        dist1_updates.update({(x + dx, y - 1): "[", (x + dx, y): "]"})
                        if (x, y - 1) not in all_updates:
                            all_updates[(x, y - 1)] = "."

            if any_wall:  # Cannot make a move.
                break

            if all_spaces:  # Can make a move.
                for (x, y), ch in all_updates.items():
                    warehouse[x][y] = ch
                rx, ry = rx + dx, ry + dy
                break

            dist += 1
            dist_updates = dist1_updates
            all_updates.update(dist_updates)

        # for x in range(size):
        #     print("".join(warehouse[x]))

    gps_sum = sum(100 * x + y for x in range(size) for y in range(2 * size) if warehouse[x][y] == "[")
    print(gps_sum)


solve("input-test-3.txt")  # 618
solve("input-test-2.txt")  # 9021
solve("input.txt")  # 1543338
