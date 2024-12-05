def solve(path):
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    left_list = []
    right_list = []

    for line in lines:
        left, right = map(int, line.split("   "))
        left_list.append(left)
        right_list.append(right)

    left_list.sort()
    right_list.sort()

    total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))
    print(total_distance)


def main():
    solve("input-test.txt")  # 11
    solve("input.txt")  # 1320851


if __name__ == "__main__":
    main()
