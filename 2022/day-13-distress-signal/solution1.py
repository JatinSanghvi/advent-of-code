def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right

    if isinstance(left, int): left = [left]
    if isinstance(right, int): right = [right]

    for left_item, right_item in zip(left, right):
        comparison = compare(left_item, right_item)
        if comparison != 0:
            return comparison

    return len(left) - len(right)


def solve(path):
    with open(path) as file:
        lines = [line.rstrip('\n') for line in file.readlines() if line != '\n']

    sum = 0
    for pair_index in range(len(lines) // 2):
        if compare(eval(lines[2 * pair_index]), eval(lines[2 * pair_index + 1])) <= 0:
            sum += pair_index + 1

    print(sum)


def main():
    solve('input-test.txt')  # 13       
    solve('input.txt')  # 5938


if __name__ == '__main__':
    main()
