import math


def solve(path):
    with open(path) as file:
        lines = file.readlines()

    heights = [[int(height) for height in line.rstrip()] for line in lines]

    rows = len(heights)
    columns = len(heights[0])

    flows = [[(row, col) for col in range(columns)] for row in range(rows)]

    # Calculate adjacent point with minimum height.
    for row in range(rows):
        for col in range(columns):
            height = heights[row][col]
            if height == 9: continue

            min_height = height
            min_index = (row, col)

            if row != 0 and heights[row - 1][col] < min_height:
                min_height = heights[row - 1][col]
                min_index = (row - 1, col)
            if row != rows - 1 and heights[row + 1][col] < min_height:
                min_height = heights[row + 1][col]
                min_index = (row + 1, col)
            if col != 0 and heights[row][col - 1] < min_height:
                min_height = heights[row][col - 1]
                min_index = (row, col - 1)
            if col != columns - 1 and heights[row][col + 1] < min_height:
                min_height = heights[row][col + 1]
                min_index = (row, col + 1)

            flows[row][col] = min_index

    # Calculate point in range with minimum height.
    for row in range(rows):
        for col in range(columns):
            (row2, col2) = (row, col)
            while (flows[row2][col2] != (row2, col2)):
                (row2, col2) = flows[row2][col2]
            flows[row][col] = (row2, col2)

    flow_list = [flow for flows in flows for flow in flows]
    basin_sizes = list(map(flow_list.count, set(flow_list)))
    print(math.prod(sorted(basin_sizes, reverse=True)[0:3]))


solve("input-test.txt")
solve("input.txt")
