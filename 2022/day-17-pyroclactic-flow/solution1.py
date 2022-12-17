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
    jet_index = 0

    for rock_index in range(2022):

        # Have enough space to fit in the largest rock at the point when it begins to fall.
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
                chamber_height = max(chamber_height, max(y for y, x in rock))
                falling = False

            jet_index += 1

    # print('\n'.join(''.join(row) for row in reversed(chamber)))
    print(chamber_height)


def main():
    solve('input-test.txt')  # 3068
    solve('input.txt')  #


if __name__ == '__main__':
    main()
