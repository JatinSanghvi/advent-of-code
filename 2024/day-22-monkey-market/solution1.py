def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    sum_secrets = 0
    for line in lines:
        secret = int(line)
        for _ in range(2000):
            secret = (secret ^ (secret * 64)) % 16777216
            secret = (secret ^ (secret) // 32) % 16777216
            secret = (secret ^ (secret * 2048)) % 16777216
        sum_secrets += secret

    print(sum_secrets)


solve("input-test-1.txt")  # 37327623
solve("input.txt")  # 15608699004
