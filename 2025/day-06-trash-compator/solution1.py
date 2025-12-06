import math


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    all_nums = [[int(val) for val in line.split()] for line in lines[:-1]]

    total = 0
    for i, operator in enumerate(lines[-1].split()):
        if operator == "+":
            total += sum(nums[i] for nums in all_nums)
        else:
            total += math.prod(nums[i] for nums in all_nums)

    print(total)


solve("input-test.txt")  # 4277556
solve("input.txt")  # 4387670995909
