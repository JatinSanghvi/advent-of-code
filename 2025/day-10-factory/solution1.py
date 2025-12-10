def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    sum_min_presses = 0
    for line in lines:
        first, *middle, _ = line.split()
        req_lights = [ch == "#" for ch in first[1:-1]]
        buttons = [[int(pos) for pos in mid[1:-1].split(",")] for mid in middle]

        min_presses = len(buttons)
        for set_num in range(1 << len(buttons)):
            lights = [False] * len(req_lights)
            presses = 0
            for button_num, button in enumerate(buttons):
                if (1 << button_num) & set_num != 0:
                    for pos in button:
                        lights[pos] = not (lights[pos])
                    presses += 1

            if lights == req_lights:
                min_presses = min(min_presses, presses)

        sum_min_presses += min_presses

    print(sum_min_presses)


# Faster implementation (source: github.com/RussellDash332/advent-of-code).
def solve2(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    sum_presses = 0
    for line in lines:
        light_str, *button_strs, _ = line.split()
        req_hash = sum((ch == "#") << i for i, ch in enumerate(light_str[1:-1]))
        num_lights = len(light_str) - 2

        buttons = [[*map(int, button_str[1:-1].split(","))] for button_str in button_strs]
        button_hashes = [sum(1 << pos for pos in button) for button in buttons]

        hash_presses = [-1] * (1 << num_lights)
        hash_presses[0] = 0

        seen_hashes = [0]
        for seen_hash in seen_hashes:
            for button_hash in button_hashes:
                hash = seen_hash ^ button_hash
                if hash_presses[hash] == -1:
                    hash_presses[hash] = hash_presses[seen_hash] + 1
                    seen_hashes.append(hash)

        sum_presses += hash_presses[req_hash]

    print(sum_presses)


solve2("input-test.txt")  # 7
solve2("input.txt")  # 522
