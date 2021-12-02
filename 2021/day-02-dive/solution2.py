def solve(path):
    with open(path) as file:
        positions = [line.split() for line in file.readlines()]

    aim = 0
    horz = 0
    depth = 0
    
    for pos in positions:
        x = int(pos[1])
        if (pos[0] == "down"): aim += x
        elif (pos[0] == "up"): aim -= x
        elif (pos[0] == "forward"): horz += x; depth += aim * x

    print(horz * depth)


solve("input-test.txt")
solve("input.txt")
