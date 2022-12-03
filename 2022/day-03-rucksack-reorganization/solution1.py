def solve(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file.readlines()]

    priority_sum = 0

    for line in lines:
        items = len(line)
        comp1 = set(line[:items // 2])
        comp2 = set(line[items // 2:])
        shared = list(comp1 & comp2)[0]
        priority = ord(shared) + (-ord('a') if ('a' <= shared <= 'z') else -ord('A') + 26) + 1
        priority_sum += priority

    print(priority_sum)


def main():
    solve('input-test.txt')  # 157
    solve('input.txt')  # 7674


if __name__ == '__main__':
    main()
