from typing import List, Set


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    a, b, c = 0, 0, 0
    program = list(map(int, lines[4].rsplit(" ", 1)[1].split(",")))

    def get_operand(opcode: int, val: int) -> int:
        if opcode in (1, 3) or val < 4:
            return val
        else:
            return a if val == 4 else b if val == 5 else c

    def get_output() -> List[int]:
        nonlocal a, b, c

        output: List[int] = []
        ip = 0  # Instruction pointer.
        while ip < len(program):
            opcode = program[ip]
            operand = get_operand(opcode, program[ip + 1])

            if opcode == 0:  # adv
                a = a // 2**operand
            elif opcode == 1:  # bxl
                b ^= operand
            elif opcode == 2:  # bst
                b = operand % 8
            elif opcode == 3:  # jnz
                if a != 0:
                    ip = operand
                    continue
            elif opcode == 4:  # bxc
                b ^= c
            elif opcode == 5:  # out
                output.append(operand % 8)
            elif opcode == 6:  # bdv
                b = a // 2**operand
            elif opcode == 7:  # cdv
                c = a // 2**operand

            ip += 2

        return output

    # Start by constructing the end of program and then iterate to construct
    # towards the start.
    a_vals = set([0])
    new_a_vals: Set[int] = set()
    for start in range(len(program) - 1, -1, -1):
        for a_val in a_vals:
            for new_a_val in range(a_val << 3, (a_val + 1) << 3):
                a = new_a_val
                if get_output() == program[start:]:
                    new_a_vals.add(new_a_val)

        a_vals = new_a_vals
        new_a_vals = set()

    print(min(a_vals))


solve("input-test-2.txt")  # 117440
solve("input.txt")  # 37221334433268
