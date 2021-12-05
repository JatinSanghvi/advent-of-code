def solve(path):
    with open(path) as file:
        lines = file.readlines()

    draws = [int(num) for num in lines[0].rstrip().split(",")]

    boards = [[[int(num) for num in line.rstrip().split()] for line in lines[index + 1:index + 6]]
              for index in range(1, len(lines), 6)]
    boards += [list(map(list, zip(*board))) for board in boards]  # Append transposed boards.

    for draw in draws:
        for board in boards:
            for line in board:
                for num_index, num in enumerate(line):
                    if num == draw:
                        line[num_index] = -1  # Mark number.

                        if all(num == -1 for num in line):
                            total = sum(sum(max(num, 0) for num in line) for line in board)
                            print(total * draw)
                            return


solve("input-test.txt")
solve("input.txt")
