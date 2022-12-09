from typing import List, Set, Tuple


def solve(path):
    motions: List[Tuple[str, int]]

    with open(path) as file:
        motions = [(line[0], int(line[2:])) for line in file.readlines()]

    tails: Set[Tuple[int, int]] = set()
    head = tail = (0, 0)

    for motion in motions:
        for _ in range(motion[1]):

            match motion[0]:
                case 'U':
                    head = (head[0], head[1] - 1)
                    if tail[1] - head[1] == 2: tail = (head[0], tail[1] - 1)
                case 'D':
                    head = (head[0], head[1] + 1)
                    if head[1] - tail[1] == 2: tail = (head[0], tail[1] + 1)
                case 'L':
                    head = (head[0] - 1, head[1])
                    if tail[0] - head[0] == 2: tail = (tail[0] - 1, head[1])
                case 'R':
                    head = (head[0] + 1, head[1])
                    if head[0] - tail[0] == 2: tail = (tail[0] + 1, head[1])

            tails.add(tail)

    print(len(tails))


def main():
    solve('input-test-1.txt')  # 13
    solve('input.txt')  # 6376


if __name__ == '__main__':
    main()
