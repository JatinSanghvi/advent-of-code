def solve(path):
    with open(path) as file:
        positions = [line.split() for line in file.readlines()]

    horz = sum(int(pos[1]) for pos in filter(lambda pos: pos[0] == "forward", positions))
    vert = sum(int(pos[1]) for pos in filter(lambda pos: pos[0] == "down", positions)) - \
        sum(int(pos[1]) for pos in filter(lambda pos: pos[0] == "up", positions))

    print(horz * vert)


solve("input-test.txt")
solve("input.txt")
