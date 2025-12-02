def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        line = file.read()

    sum = 0
    for id_range in line.split(","):
        (start, end) = (int(token) for token in id_range.split("-"))
        for id in range(start, end + 1):
            str_id = str(id)
            len_id = len(str_id)
            for splits in [2, 3, 5, 7]:
                if len_id % splits == 0:
                    size = len_id // splits
                    digits = str_id[:size]
                    for seg in range(1, splits):
                        if str_id[seg * size : (seg + 1) * size] != digits:
                            break
                    else:
                        sum += id
                        break

    print(sum)


solve("input-test.txt")  # 4174379265
solve("input.txt")  # 49046150754
