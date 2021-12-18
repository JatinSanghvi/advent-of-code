import re


def solve(path):
    with open(path) as file:
        line = file.readline()

    match = re.match("^target area: x=(.*?)\.\.(.*?), y=(.*?)\.\.(.*?)$", line)
    min_yrange = int(match.groups()[2])

    # y positions: y, 2y-1, .., y(y+1)/2, .., 2y-1, y, 0, -y-1
    max_yvelocity = - min_yrange - 1
    max_ypos = max_yvelocity * (max_yvelocity + 1) // 2
    print(max_ypos)


solve("input-test.txt")
solve("input.txt")
