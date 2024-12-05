def solve(path):
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    safe_count = 0

    for line in lines:
        levels = list(map(int, line.split()))
        diffs = [levels[i] - levels[i + 1] for i in range(len(levels) - 1)]
        max_diff, min_diff = max(diffs), min(diffs)

        if (min_diff >= -3 and max_diff <= -1) or (min_diff >= 1 and max_diff <= 3):
            safe_count += 1

    print(safe_count)


def main():
    solve("input-test.txt")  # 2
    solve("input.txt")  # 220


if __name__ == "__main__":
    main()
