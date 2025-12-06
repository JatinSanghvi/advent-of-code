import math

from typing import List


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line for line in file.readlines()]

    total = 0
    nums: List[int] = []

    for pos in range(len(lines[0])):
        if lines[-1][pos] in ["+", "*"]:
            operator = lines[-1][pos]

        str_num = "".join([digit for line in lines[:-1] if "0" <= (digit := line[pos]) <= "9"])
        if str_num == "":
            if operator == "+":
                total += sum(num for num in nums)
            else:
                total += math.prod(num for num in nums)
            nums = []
        else:
            nums.append(int(str_num))

    print(total)


solve("input-test.txt")  # 3263827
solve("input.txt")  # 9625320374409
