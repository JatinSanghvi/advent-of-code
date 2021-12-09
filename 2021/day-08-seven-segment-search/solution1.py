def solve(path):
    with open(path) as file:
        lines = file.readlines()

    outputs = [line.split(" | ")[1].split() for line in lines]
    digit_count = sum(len(digit) in [2, 3, 4, 7] for output in outputs for digit in output)
    print(digit_count)


solve("input-test.txt")
solve("input.txt")
