def solve(path):
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    safe_count = 0

    for line in lines:
        levels = list(map(int, line.split()))

        for index in range(len(levels)):
            new_levels = levels[:index] + levels[index + 1 :]
            diffs = [new_levels[i] - new_levels[i + 1] for i in range(len(new_levels) - 1)]
            max_diff, min_diff = max(diffs), min(diffs)

            if (min_diff >= -3 and max_diff <= -1) or (min_diff >= 1 and max_diff <= 3):
                safe_count += 1
                break

    print(safe_count)


def main():
    solve("input-test.txt")  # 4
    solve("input.txt")  # 296


if __name__ == "__main__":
    main()
