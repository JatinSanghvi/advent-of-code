import re


def solve(path):
    with open(path) as file:
        lines = file.readlines()

    cube = [False] * 101 * 101 * 101
    pattern = re.compile("(.*?) x=(.*?)\.\.(.*?),y=(.*?)\.\.(.*?),z=(.*?)\.\.(.*?)")
    for line in lines:
        match = pattern.fullmatch(line.rstrip())

        value = match[1] == "on"
        xmin = max(-50, int(match[2]))
        xmax = min(50, int(match[3]))
        ymin = max(-50, int(match[4]))
        ymax = min(50, int(match[5]))
        zmin = max(-50, int(match[6]))
        zmax = min(50, int(match[7]))

        for x in range(xmin, xmax + 1):
            index1 = (x + 50) * 101 * 101
            for y in range(ymin, ymax + 1):
                index2 = index1 + (y + 50) * 101
                for z in range(zmin, zmax + 1):
                    index3 = index2 + (z + 50)
                    cube[index3] = value

    print(sum(cube))


solve("input-test-1.txt")
solve("input.txt")
