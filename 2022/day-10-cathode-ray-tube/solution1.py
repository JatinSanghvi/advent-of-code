def solve(path):
    with open(path) as file:
        lines = [line.rstrip('\n') for line in file.readlines()]

    x = 1
    cycle = 0
    signal = 0

    for line in lines:
        (cycles, new_x) = (1, x) if line == 'noop' else (2, x + int(line.split()[-1]))

        for _ in range(cycles):
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                signal += cycle * x
        x = new_x

    print(signal)


def main():
    solve('input-test.txt')  # 13140
    solve('input.txt')  # 14340


if __name__ == '__main__':
    main()
