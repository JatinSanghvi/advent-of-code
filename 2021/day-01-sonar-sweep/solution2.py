def solve(path):
    with open(path) as file:
        depths = [int(line) for line in file.readlines()]

    print(sum(depths[index] > depths[index - 3] for index in range(3, len(depths))))


solve("input-test.txt")
solve("input.txt")
