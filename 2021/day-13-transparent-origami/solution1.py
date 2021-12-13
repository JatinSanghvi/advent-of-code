import re


def solve(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file.readlines()]

    divider = lines.index("")
    dots = set(tuple(int(coor) for coor in line.split(",")) for line in lines[:divider])

    match = re.search("fold along ([x|y])=(\d+)", lines[divider + 1])
    axis = match.group(1)
    line_location = int(match.group(2))

    def modx(x): return min(x, 2 * line_location - x) if axis == "x" else x
    def mody(y): return min(y, 2 * line_location - y) if axis == "y" else y

    folded_dots = set((modx(dot[0]), mody(dot[1])) for dot in dots)
    print(len(folded_dots))


solve("input-test.txt")
solve("input.txt")
