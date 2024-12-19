from typing import List


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    a, b, c = (int(lines[i].rsplit(" ", 1)[1]) for i in [0, 1, 2])
    program = list(map(int, lines[4].rsplit(" ", 1)[1].split(",")))

    def get_operand(opcode: int, value: int) -> int:
        if opcode in (1, 3) or value < 4:
            return value
        else:
            return a if value == 4 else b if value == 5 else c

    output: List[int] = []
    ip = 0
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

    print(",".join(map(str, output)))


solve("input-test-1.txt")  # 4,6,3,5,6,3,5,2,1,0
solve("input.txt")  # 3,7,1,7,2,1,0,6,3
