def solve(path):
    with open(path) as file:
        lines = file.readlines()

    dimensions = [[int(dim) for dim in line.split('x')] for line in lines]
    ribbon_lengths = [2 * (dims[0] + dims[1] + dims[2] - max(dims)) + dims[0] * dims[1] * dims[2] for dims in dimensions]
    print(sum(ribbon_lengths))


def main():
    solve('input-test.txt')  # 48
    solve('input.txt')  # 3842356


if __name__ == '__main__':
    main()
