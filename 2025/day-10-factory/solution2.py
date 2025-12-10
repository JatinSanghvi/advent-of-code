import pulp  # type: ignore


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    sum_presses = 0
    for line in lines:
        _, *button_strs, joltage_str = line.split()

        req_joltages = [*map(int, joltage_str[1:-1].split(","))]
        buttons = [[*map(int, button_str[1:-1].split(","))] for button_str in button_strs]

        coeff_vars = [pulp.LpVariable(str(b), lowBound=0, cat=pulp.const.LpInteger) for b in range(len(buttons))]

        prob = pulp.LpProblem()
        for pos, joltage in enumerate(req_joltages):  # Constraints.
            combinations = [int(pos in button) for button in buttons]
            prob += sum(coeff_vars[b] * combinations[b] for b in range(len(buttons))) == joltage
        prob += sum(coeff_vars)  # Objective: minimize sum of coefficients.

        prob.solve(pulp.PULP_CBC_CMD(msg=False))
        sum_presses += round(pulp.value(sum(coeff_vars)))

    print(sum_presses)


solve("input-test.txt")  # 33
solve("input.txt")  # 18105
