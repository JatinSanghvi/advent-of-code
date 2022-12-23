import re

def solve(path):
    with open(path) as file:
        lines = [line.rstrip('\n') for line in file.readlines()]

    map_ = [line for line in lines[:-2]]

    rows = len(map_)
    cols = max(len(line) for line in map_)

    col_mins, col_maxs, row_mins, row_maxs = [], [], [0] * cols, [rows] * cols

    pattern = re.compile(r'#|\.')
    prev_col_min, prev_col_max = cols, 0

    for row, line in enumerate(map_):
        col_min = pattern.search(line).start()
        col_max = len(line)

        col_mins.append(col_min)
        col_maxs.append(col_max)

        if col_min < prev_col_min:
            for col in range(col_min, prev_col_min): row_mins[col] = row
        elif col_min > prev_col_min:
            for col in range(prev_col_min, col_min): row_maxs[col] = row

        if col_max > prev_col_max:
            for col in range(prev_col_max, col_max): row_mins[col] = row
        if col_max < prev_col_max:
            for col in range(col_max, prev_col_max): row_maxs[col] = row

        prev_col_min = col_min
        prev_col_max = col_max

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir = 0
    row, col = 0, pattern.search(map_[0]).start()

    pattern = re.compile(r'L|R|\d+')
    path = lines[-1]

    for step in pattern.findall(path):
        if step == 'L': dir = (dir - 1) % len(moves)
        elif step == 'R': dir = (dir + 1) % len(moves)
        else:
            for _ in range(int(step)):
                new_row, new_col = row + moves[dir][0], col + moves[dir][1]
                if new_row >= row_maxs[col]: new_row = row_mins[col]
                if new_row < row_mins[col]: new_row = row_maxs[col] - 1
                if new_col >= col_maxs[row]: new_col = col_mins[row]
                if new_col < col_mins[row]: new_col = col_maxs[row] - 1

                if map_[new_row][new_col] == '#':
                    break
                else:
                    row, col = new_row, new_col

    print(1000 * (row + 1) + 4 * (col + 1) + dir)


def main():
    solve('input-test.txt')  # 6032
    solve('input.txt')  # 57350


if __name__ == '__main__':
    main()
