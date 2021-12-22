import re


def solve(path):
    with open(path) as file:
        lines = file.readlines()

    pos1 = int(re.search("^Player 1 starting position: (\d+)$", lines[0]).groups()[0])
    pos2 = int(re.search("^Player 2 starting position: (\d+)$", lines[1]).groups()[0])
    wins_cache = {}
    rolls = [r1 + r2 + r3 for r1 in [1, 2, 3] for r2 in [1, 2, 3] for r3 in [1, 2, 3]]

    def wins(pos1, pos2, score1, score2):
        if score1 >= 21: return (1, 0)
        if score2 >= 21: return (0, 1)

        if (pos1, pos2, score1, score2) not in wins_cache:
            wins21 = [wins(pos2, new_pos1 := (pos1 + roll - 1) % 10 + 1, score2, score1 + new_pos1) for roll in rolls]
            wins2 = sum(wins[0] for wins in wins21)
            wins1 = sum(wins[1] for wins in wins21)
            wins_cache[(pos1, pos2, score1, score2)] = (wins1, wins2)

        return wins_cache[(pos1, pos2, score1, score2)]

    print(max(wins(pos1, pos2, 0, 0)))


solve("input-test.txt")
solve("input.txt")
