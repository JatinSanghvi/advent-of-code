def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        line = file.read()

    sum = 0
    for id_range in line.split(","):
        (start, end) = (int(token) for token in id_range.split("-"))
        for id in range(start, end + 1):
            str_id = str(id)
            len_id = len(str_id)
            if str_id[: (len_id // 2)] == str_id[(len_id // 2) :]:
                sum += id

    print(sum)


solve("input-test.txt")  # 1227775554
solve("input.txt")  # 38437576669
