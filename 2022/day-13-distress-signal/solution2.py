import functools


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

    packets = [eval(line) for line in lines]
    div1, div2 = [[2]], [[6]]
    packets.append(div1)
    packets.append(div2)

    packets.sort(key=functools.cmp_to_key(compare))

    print((packets.index(div1) + 1) * (packets.index(div2) + 1))


def main():
    solve('input-test.txt')  # 140
    solve('input.txt')  # 29025


if __name__ == '__main__':
    main()
