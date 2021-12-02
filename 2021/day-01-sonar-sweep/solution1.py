def solve(path):
    with open(path) as file:
        depths = [int(line) for line in file.readlines()]

    print(sum(depths[index] > depths[index - 1] for index in range(1, len(depths))))


solve("input-test.txt")
solve("input.txt")
