import re


def solve(path):
    with open(path) as file:
        lines = file.readlines()

    positions = [
        int(re.search("^Player 1 starting position: (\d+)$", lines[0]).groups()[0]),
        int(re.search("^Player 2 starting position: (\d+)$", lines[1]).groups()[0])
    ]

    scores = [0, 0]
    roll = 7

    for turn in range(2000):
        roll = (roll - 1) % 10
        index = turn % 2
        positions[index] = (positions[index] + roll - 1) % 10 + 1
        scores[index] += positions[index]
        if scores[index] >= 1000:
            break

    print(scores[(turn + 1) % 2] * (turn + 1) * 3)


solve("input-test.txt")
solve("input.txt")
