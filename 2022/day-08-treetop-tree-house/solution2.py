def solve(path):
    with open(path) as file:
        trees = [[int(char) for char in line.rstrip('\n')] for line in file.readlines()]

    rows, cols = len(trees), len(trees[0])
    max_score = 0

    for row in range(rows):
        for col in range(cols):

            height = trees[row][col]
            up_row = down_row = row
            left_col = right_col = col

            for up_row in range(row - 1, -1, -1):
                if trees[up_row][col] >= height:
                    break

            for down_row in range(row + 1, rows):
                if trees[down_row][col] >= height:
                    break

            for left_col in range(col - 1, -1, -1):
                if trees[row][left_col] >= height:
                    break

            for right_col in range(col + 1, cols):
                if trees[row][right_col] >= height:
                    break

            max_score = max(max_score, (row - up_row) * (down_row - row) * (col - left_col) * (right_col - col))

    print(max_score)


def main():
    solve('input-test.txt')  # 8
    solve('input.txt')  # 284648


if __name__ == '__main__':
    main()
