def solve(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file.readlines()]

    score = 0

    for line in lines:
        [opp, me] = line.split()

        if me == 'X':
            score += 0 + {'A': 3, 'B': 1, 'C': 2}[opp]
        elif me == 'Y':
            score += 3 + {'A': 1, 'B': 2, 'C': 3}[opp]
        elif me == 'Z':
            score += 6 + {'A': 2, 'B': 3, 'C': 1}[opp]

    print(score)


def main():
    solve('input-test.txt')  # 12
    solve('input.txt')  # 16862


if __name__ == '__main__':
    main()
