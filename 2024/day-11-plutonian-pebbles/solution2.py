from typing import List
import functools


# Returns next stones after a single blink
def new_stones(stone: int) -> List[int]:
    if stone == 0:
        return [1]

    stone_str = str(stone)
    len_str = len(stone_str)
    if len_str % 2 == 0:
        return [int(stone_str[: len_str // 2]), int(stone_str[len_str // 2 :])]

    return [stone * 2024]


# Uses recursion and memoization to compute stone count
@functools.cache
def get_stone_count(stone: int, blinks: int) -> int:
    return 1 if blinks == 0 else sum(get_stone_count(new_stone, blinks - 1) for new_stone in new_stones(stone))


def solve(path: str, blinks: int) -> None:
    with open(path, encoding="utf-8") as file:
        line = file.readline().rstrip("\n")

    stones = list(map(int, line.split()))
    print(sum(get_stone_count(stone, blinks) for stone in stones))


solve("input-test.txt", 25)  # 55312
solve("input.txt", 75)  # 241651071960597
