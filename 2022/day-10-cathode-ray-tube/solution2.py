def solve(path):
    with open(path) as file:
        lines = [line.rstrip('\n') for line in file.readlines()]

    x = 1
    cycle = 1

    for line in lines:
        (cycles, new_x) = (1, x) if line == 'noop' else (2, x + int(line.split()[-1]))

        for _ in range(cycles):
            print('#' if x <= ((cycle - 1) % 40 + 1) <= x + 2 else '.', end='')
            cycle += 1
            if cycle % 40 == 1:
                print()
        x = new_x

    print()


def main():
    # ##..##..##..##..##..##..##..##..##..##..
    # ###...###...###...###...###...###...###.
    # ####....####....####....####....####....
    # #####.....#####.....#####.....#####.....
    # ######......######......######......####
    # #######.......#######.......#######.....
    solve('input-test.txt')

    # ###...##..###....##..##..###..#..#.###..
    # #..#.#..#.#..#....#.#..#.#..#.#..#.#..#.
    # #..#.#..#.#..#....#.#....###..####.#..#.
    # ###..####.###.....#.#....#..#.#..#.###..
    # #....#..#.#....#..#.#..#.#..#.#..#.#....
    # #....#..#.#.....##...##..###..#..#.#....
    solve('input.txt')


if __name__ == '__main__':
    main()
