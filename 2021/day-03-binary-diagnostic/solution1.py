def solve(path):
    with open(path) as file:
        matrix = [[int(bit) for bit in line.rstrip()] for line in file.readlines()]

    gamma_arr = [max(set(pos), key=pos.count) for pos in zip(*matrix)]
    epsilon_arr = [1 if bit == 0 else 0 for bit in gamma_arr]

    gamma = int("".join(str(bit) for bit in gamma_arr), 2)
    epsilon = int("".join(str(bit) for bit in epsilon_arr), 2)

    print(gamma * epsilon)


solve("input-test.txt")
solve("input.txt")
