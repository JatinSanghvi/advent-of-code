import math


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        input_ = file.read()

    *shape_strs, region_str = input_.split("\n\n")
    gift_sizes = [s.count("#") for s in shape_strs]
    regions = [region for region in region_str.split("\n") if region]

    # It is a trick problem. All input areas are either marginally smaller (by 1 to 3 blocks) than the total area of
    # gifts, or are too large to fit all of them comfortably.
    can_fit = 0
    for region in regions:
        dim_str, count_str = region.split(": ")
        tree_area = math.prod(map(int, dim_str.split("x")))
        gift_counts = map(int, count_str.split())
        gift_area = sum(count * size for count, size in zip(gift_counts, gift_sizes))
        can_fit += tree_area >= gift_area

    print(can_fit)


solve("input-test.txt")  # 3 (incorrect)
solve("input.txt")  # 481
