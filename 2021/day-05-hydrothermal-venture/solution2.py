import re


def solve(path):
    with open(path) as file:
        lines = file.readlines()

    segments = [[int(point) for point in re.split(" -> |,", line.rstrip())] for line in lines]

    points = {}

    for seg in segments:
        inc_x = 1 if seg[2] > seg[0] else -1 if seg[2] < seg[0] else 0
        inc_y = 1 if seg[3] > seg[1] else -1 if seg[3] < seg[1] else 0
        start = (seg[0], seg[1])
        end = (seg[2] + inc_x, seg[3] + inc_y)

        point = start
        while point != end:
            if point not in points: points[point] = 0
            points[point] += 1
            point = (point[0] + inc_x, point[1] + inc_y)

    print(len([point for point in points if points[point] > 1]))


solve("input-test.txt")
solve("input.txt")
