import re


def solve(path):
    with open(path) as file:
        line = file.readline()

    match = re.match("^target area: x=(.*?)\.\.(.*?), y=(.*?)\.\.(.*?)$", line)
    [min_xrange, max_xrange, min_yrange, max_yrange] = [int(group) for group in match.groups()]

    max_moves = 2 * (- min_yrange) + 1  # y, 2y-1, .., y(y+1)/2, y(y+1)/2, .., 2y-1, y, 0, -y-1
    xvelocities = [[] for _ in range(max_moves + 1)]
    yvelocities = [[] for _ in range(max_moves + 1)]

    for xvelocity in range(max_xrange + 1):
        xposition = 0
        xincrement = xvelocity
        for moves in range(max_moves + 1):
            if xposition > max_xrange: break
            if xposition >= min_xrange: xvelocities[moves].append(xvelocity)
            xposition += xincrement
            xincrement = max(xincrement - 1, 0)

    for yvelocity in range(min_yrange, - min_yrange):
        yposition = 0
        yincrement = yvelocity
        for moves in range(max_moves + 1):
            if yposition < min_yrange: break
            if yposition <= max_yrange: yvelocities[moves].append(yvelocity)
            yposition += yincrement
            yincrement = yincrement - 1

    # Handle the case when the probe will land multiple times in target area for the same x and y velocities.
    velocity_set = set()
    for (xvs, yvs) in zip(xvelocities, yvelocities):
        velocity_set |= set((xv, yv) for xv in xvs for yv in yvs)

    print(len(velocity_set))


solve("input-test.txt")
solve("input.txt")
