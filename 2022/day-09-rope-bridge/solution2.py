from typing import List, Set, Tuple


def solve(path):
    motions: List[Tuple[str, int]]

    with open(path) as file:
        motions = [(line[0], int(line[2:])) for line in file.readlines()]

    tails: Set[Tuple[int, int]] = set()
    knots = 10 * [(0, 0)]

    for motion in motions:
        for _ in range(motion[1]):
            match motion[0]:
                case 'U': knots[0] = (knots[0][0], knots[0][1] - 1)
                case 'D': knots[0] = (knots[0][0], knots[0][1] + 1)
                case 'L': knots[0] = (knots[0][0] - 1, knots[0][1])
                case 'R': knots[0] = (knots[0][0] + 1, knots[0][1])

            for ki in range(1, 10):
                disjoint = \
                    knots[ki][0] > knots[ki - 1][0] + 1 or \
                    knots[ki][0] < knots[ki - 1][0] - 1 or \
                    knots[ki][1] > knots[ki - 1][1] + 1 or \
                    knots[ki][1] < knots[ki - 1][1] - 1

                if disjoint:
                    knots[ki] = (
                        knots[ki][0] + (-1 if knots[ki - 1][0] < knots[ki][0] else 1 if knots[ki - 1][0] > knots[ki][0] else 0),
                        knots[ki][1] + (-1 if knots[ki - 1][1] < knots[ki][1] else 1 if knots[ki - 1][1] > knots[ki][1] else 0))

            tails.add(knots[9])

    print(len(tails))


def main():
    solve('input-test-1.txt')  # 1
    solve('input-test-2.txt')  # 36
    solve('input.txt')  # 2607


if __name__ == '__main__':
    main()
