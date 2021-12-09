def solve(path):
    with open(path) as file:
        lines = file.readlines()

    heights = [[height for height in line.rstrip()] for line in lines]

    risk_sum = 0
    rows = len(heights)
    columns = len(heights[0])

    for row in range(rows):
        for col in range(columns):
            height = heights[row][col]
            if (row == 0 or height < heights[row - 1][col]) \
                    and (row == rows - 1 or height < heights[row + 1][col]) \
                    and (col == 0 or height < heights[row][col - 1]) \
                    and (col == columns - 1 or height < heights[row][col + 1]):
                risk_sum += int(height) + 1

    print(risk_sum)


solve("input-test.txt")
solve("input.txt")
