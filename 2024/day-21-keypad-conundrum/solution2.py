from typing import List, Set
import functools


def solve(path: str, robots: int) -> None:
    num_keypad = {
        "7": (0, 0),
        "8": (0, 1),
        "9": (0, 2),
        "4": (1, 0),
        "5": (1, 1),
        "6": (1, 2),
        "1": (2, 0),
        "2": (2, 1),
        "3": (2, 2),
        "X": (3, 0),
        "0": (3, 1),
        "A": (3, 2),
    }

    dir_keypad = {
        "X": (0, 0),
        "^": (0, 1),
        "A": (0, 2),
        "<": (1, 0),
        "v": (1, 1),
        ">": (1, 2),
    }

    @functools.cache
    def get_keys(from_key: str, to_key: str, use_num_keypad: bool) -> Set[str]:
        keypad = num_keypad if use_num_keypad else dir_keypad
        out_keys: Set[str] = set()
        (fr, fc), (tr, tc) = keypad[from_key], keypad[to_key]

        if keypad["X"] != (tr, fc):
            keys = ["v" for _ in range(fr, tr)] + ["^" for _ in range(tr, fr)] + [">" for _ in range(fc, tc)] + ["<" for _ in range(tc, fc)] + ["A"]
            out_keys.add("".join(keys))

        if keypad["X"] != (fr, tc):
            keys = [">" for _ in range(fc, tc)] + ["<" for _ in range(tc, fc)] + ["v" for _ in range(fr, tr)] + ["^" for _ in range(tr, fr)] + ["A"]
            out_keys.add("".join(keys))

        return out_keys

    @functools.cache
    def get_sequences(code: str, use_num_keypad: bool) -> List[Set[str]]:
        return [get_keys(from_key, to_key, use_num_keypad) for from_key, to_key in zip("A" + code[:-1], code)]

    @functools.cache
    def get_min_length(code: str, robots: int, use_num_keypad) -> int:
        if robots == 0:
            return len(code)

        sequences = get_sequences(code, use_num_keypad)
        sequences_min = 0
        for options in sequences:
            sequences_min += min(get_min_length(opt, robots - 1, use_num_keypad=False) for opt in options)
        return sequences_min

    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    complexity = 0
    for line in lines:
        min_length = get_min_length(line, robots, True)
        num_value = int("".join(ch for ch in line if "0" <= ch <= "9"))
        complexity += min_length * num_value

    print(complexity)


solve("input-test.txt", 3)  # 126384
solve("input.txt", 26)  # 177814
