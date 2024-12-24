from typing import Dict, Iterable, Set, Tuple


def solve(path: str) -> None:
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

    def get_keys(from_key: str, to_key: str, keypad: Dict[str, Tuple[int, int]]) -> Set[str]:
        out_keys: Set[str] = set()
        (fr, fc), (tr, tc) = keypad[from_key], keypad[to_key]

        if keypad["X"] != (tr, fc):
            keys = ["v" for _ in range(fr, tr)] + ["^" for _ in range(tr, fr)] + [">" for _ in range(fc, tc)] + ["<" for _ in range(tc, fc)] + ["A"]
            out_keys.add("".join(keys))

        if keypad["X"] != (fr, tc):
            keys = [">" for _ in range(fc, tc)] + ["<" for _ in range(tc, fc)] + ["v" for _ in range(fr, tr)] + ["^" for _ in range(tr, fr)] + ["A"]
            out_keys.add("".join(keys))

        return out_keys

    def get_sequences(in_sequences: Iterable[str], keypad: Dict[str, Tuple[int, int]]) -> Set[str]:
        all_sequences: Set[str] = set()

        for in_seq in in_sequences:
            out_sequences = set([""])
            for from_key, to_key in zip("A" + in_seq[:-1], in_seq):
                new_out_sequences: Set[str] = set()
                for keys in get_keys(from_key, to_key, keypad):
                    for seq in out_sequences:
                        new_out_sequences.add(seq + keys)
                out_sequences = new_out_sequences
            all_sequences.update(out_sequences)

        return all_sequences

    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    complexity = 0
    for line in lines:
        robot1_seq = get_sequences([line], num_keypad)
        robot2_seq = get_sequences(robot1_seq, dir_keypad)
        robot3_seq = get_sequences(robot2_seq, dir_keypad)

        min_length = min(len(seq) for seq in robot3_seq)
        num_value = int("".join(ch for ch in line if "0" <= ch <= "9"))
        complexity += min_length * num_value

    print(complexity)


solve("input-test.txt")  # 126384
solve("input.txt")  # 177814
