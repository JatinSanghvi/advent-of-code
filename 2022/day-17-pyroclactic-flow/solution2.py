from typing import List, Tuple


def solve(path):
    with open(path) as file:
        jet = file.readline()

    # Displace rocks by three positions horizontally to account for the wall.
    rocks: List[List[Tuple[int, int]]] = [
        [(0, 3), (0, 4), (0, 5), (0, 6)],
        [(0, 4), (1, 3), (1, 4), (1, 5), (2, 4)],
        [(0, 3), (0, 4), (0, 5), (1, 5), (2, 5)],
        [(0, 3), (1, 3), (2, 3), (3, 3)],
        [(0, 3), (0, 4), (1, 3), (1, 4)],
    ]

    chamber: List[List[str]] = [['+', '-', '-', '-', '-', '-', '-', '-', '+']]
    chamber_height = 0
    height = 0

    jet_index = 0
    rock_index = 0

    prev_state: Tuple[int, int, int] = None

    while rock_index < 1_000_000_000_000:
        chamber += [['|', '.', '.', '.', '.', '.', '.', '.', '|'] for _ in range(chamber_height + 8 - len(chamber))]
        rock: List[Tuple[int, int]] = [(y + chamber_height + 4, x) for y, x in rocks[rock_index % 5]]
        falling = True

        while falling:
            new_rock = [(y, x - 1) if jet[jet_index % len(jet)] == '<' else (y, x + 1) for y, x in rock]
            if all(chamber[y][x] == '.' for y, x in new_rock):
                rock = new_rock

            new_rock = [(y - 1, x) for y, x in rock]
            if all(chamber[y][x] == '.' for y, x in new_rock):
                rock = new_rock
            else:
                for y, x in rock: chamber[y][x] = '#'
                rock_index += 1

                new_chamber_height = max(chamber_height, max(y for y, x in rock))
                height += new_chamber_height - chamber_height
                chamber_height = new_chamber_height

                falling = False

                # Some heuristics to increase the likelihood of the rock structure matching between this and previous state.
                if rock_index > len(jet) and rock_index % 5 == 0 and rock[0][1] == 3:
                    if prev_state is None:
                        prev_state = (jet_index % len(jet), rock_index, height)
                    elif prev_state[0] == jet_index % len(jet):
                        _, prev_rock_index, prev_height = prev_state
                        cycles = (1_000_000_000_000 - rock_index) // (rock_index - prev_rock_index)
                        rock_index += cycles * (rock_index - prev_rock_index)
                        height += cycles * (height - prev_height)

            jet_index += 1

    print(height)


def main():
    solve('input-test.txt')  # 1514285714288
    solve('input.txt')  # 1570434782634


if __name__ == '__main__':
    main()
