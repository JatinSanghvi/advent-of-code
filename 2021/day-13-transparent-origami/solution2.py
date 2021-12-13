import re


def solve(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file.readlines()]

    divider = lines.index("")
    dots = set(tuple(int(coor) for coor in line.split(",")) for line in lines[:divider])

    for line in lines[divider + 1:]:
        match = re.search("fold along ([x|y])=(\d+)", line)
        axis = match.group(1)
        line_location = int(match.group(2))

        def modx(x): return min(x, 2 * line_location - x) if axis == "x" else x
        def mody(y): return min(y, 2 * line_location - y) if axis == "y" else y

        dots = set((modx(dot[0]), mody(dot[1])) for dot in dots)

    max_x = max([dot[0] for dot in dots])
    max_y = max([dot[1] for dot in dots])

    for y in range(max_y + 1):
        print("".join("#" if (x, y) in dots else "." for x in range(max_x + 1)))
    print()


solve("input-test.txt")
solve("input.txt")
