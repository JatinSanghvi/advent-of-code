from typing import List, Tuple


def solve(path):
    def find_height(height: int) -> Tuple[int, int]:
        for row in range(rows):
            for col in range(cols):
                if heights[row][col] == height:
                    return (row, col)

    with open(path) as file:
        lines = [line.rstrip('\n') for line in file.readlines()]

    heights = [[ord(char) for char in line] for line in lines]
    rows, cols = len(heights), len(heights[0])

    start_loc = find_height(ord('S'))
    end_loc = find_height(ord('E'))

    heights[start_loc[0]][start_loc[1]] = ord('a')
    heights[end_loc[0]][end_loc[1]] = ord('z')

    visited = [[False] * cols for _ in range(rows)]
    visit_loc: List[Tuple[int, int]] = []
    next_visit_loc: List[Tuple[int, int]] = []

    for row in range(rows):
        for col in range(cols):
            if heights[row][col] == ord('a'):
                next_visit_loc.append((row, col))
                visited[row][col] = True

    moves = 0
    while next_visit_loc and end_loc not in next_visit_loc:
        visit_loc = next_visit_loc
        next_visit_loc = []

        for loc in visit_loc:
            row, col = loc
            height = heights[row][col]

            if row > 0 and not visited[row - 1][col] and heights[row - 1][col] <= height + 1:
                visited[row - 1][col] = True
                next_visit_loc.append((row - 1, col))
            if row < rows - 1 and not visited[row + 1][col] and heights[row + 1][col] <= height + 1:
                visited[row + 1][col] = True
                next_visit_loc.append((row + 1, col))
            if col > 0 and not visited[row][col - 1] and heights[row][col - 1] <= height + 1:
                visited[row][col - 1] = True
                next_visit_loc.append((row, col - 1))
            if col < cols - 1 and not visited[row][col + 1] and heights[row][col + 1] <= height + 1:
                visited[row][col + 1] = True
                next_visit_loc.append((row, col + 1))

        moves += 1

    print(moves)


def main():
    solve('input-test.txt')  # 29
    solve('input.txt')  # 451


if __name__ == '__main__':
    main()
