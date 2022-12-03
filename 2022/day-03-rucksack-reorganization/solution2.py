def solve(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file.readlines()]

    priority_sum = 0

    for index in range(0, len(lines), 3):
        item_sets = [{item for item in items} for items in lines[index: index + 3]]
        shared = list(item_sets[0] & item_sets[1] & item_sets[2])[0]
        priority = ord(shared) + (-ord('a') if ('a' <= shared <= 'z') else -ord('A') + 26) + 1
        priority_sum += priority

    print(priority_sum)


def main():
    solve('input-test.txt')  # 70
    solve('input.txt')  # 2805


if __name__ == '__main__':
    main()
