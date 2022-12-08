def solve(path):
    with open(path) as file:
        trees = [[int(char) for char in line.rstrip('\n')] for line in file.readlines()]

    rows, cols = len(trees), len(trees[0])
    visibles = [cols * [False] for _ in range(rows)]

    for row in range(rows):
        height = -1
        for col in range(cols):
            if height < trees[row][col]:
                height = trees[row][col]
                visibles[row][col] = True

    for row in range(rows):
        height = -1
        for col in range(cols - 1, -1, -1):
            if height < trees[row][col]:
                height = trees[row][col]
                visibles[row][col] = True

    for col in range(cols):
        height = -1
        for row in range(rows):
            if height < trees[row][col]:
                height = trees[row][col]
                visibles[row][col] = True

    for col in range(cols):
        height = -1
        for row in range(rows - 1, -1, -1):
            if height < trees[row][col]:
                height = trees[row][col]
                visibles[row][col] = True

    print(sum(sum(row) for row in visibles))


def main():
    solve('input-test.txt')  # 21
    solve('input.txt')  # 1733


if __name__ == '__main__':
    main()
