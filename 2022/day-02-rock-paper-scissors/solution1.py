def solve(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file.readlines()]

    score = 0

    for line in lines:
        [opp, me] = line.split()

        if me == 'X':
            score += 1 + {'A': 3, 'B': 0, 'C': 6}[opp]
        elif me == 'Y':
            score += 2 + {'A': 6, 'B': 3, 'C': 0}[opp]
        elif me == 'Z':
            score += 3 + {'A': 0, 'B': 6, 'C': 3}[opp]

    print(score)


def main():
    solve('input-test.txt')  # 15
    solve('input.txt')  # 11475


if __name__ == '__main__':
    main()
