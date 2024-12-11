from typing import List


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        line = file.readline().rstrip("\n")

    stones = list(map(int, line.split()))

    for _ in range(25):
        new_stones: List[int] = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
                continue

            stone_str = str(stone)
            len_str = len(stone_str)
            if len_str % 2 == 0:
                new_stones.append(int(stone_str[: len_str // 2]))
                new_stones.append(int(stone_str[len_str // 2 :]))
            else:
                new_stones.append(stone * 2024)

        stones = new_stones

    print(len(stones))


solve("input-test.txt")  # 55312
solve("input.txt")  # 204022
