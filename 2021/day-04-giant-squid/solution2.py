def solve(path):
    with open(path) as file:
        lines = file.readlines()

    draws = [int(num) for num in lines[0].rstrip().split(",")]

    boards = [[[int(num) for num in line.rstrip().split()] for line in lines[index + 1:index + 6]]
              for index in range(1, len(lines), 6)]

    boards = [list(board + list(map(list, zip(*board)))) for board in boards]  # Append transposed lines to each board.

    for draw in draws:
        for board in boards:
            for line in board:
                for num_index, num in enumerate(line):
                    if num == draw:
                        line[num_index] = -1  # Mark number.

        new_boards = list(filter(lambda board: not any(all(num == -1 for num in line) for line in board), boards))

        if not new_boards:
            total = sum(sum(max(num, 0) for num in line) for line in boards[0])
            print(total * draw // 2)  # Should account numbers in transposed lines.
            return

        boards = new_boards


solve("input-test.txt")
solve("input.txt")
