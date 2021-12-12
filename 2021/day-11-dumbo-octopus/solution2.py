def solve(path):
    with open(path) as file:
        lines = file.readlines()

    # Add matrix border to simplify code.
    energies = [[int(char) for char in line.rstrip() + "0"] for line in lines + ["0000000000"]]

    steps = 0
    flashes = 0

    while flashes < 100:
        flashes = 0
        energies = [[energy + 1 for energy in energy_row] for energy_row in energies]

        while True:
            new_flashes = 0
            for row in range(10):
                for col in range(10):
                    if (energies[row][col] >= 10):
                        new_flashes += 1
                        energies[row][col] = 0
                        if energies[row - 1][col - 1] != 0: energies[row - 1][col - 1] += 1
                        if energies[row - 1][col + 1] != 0: energies[row - 1][col + 1] += 1
                        if energies[row + 1][col - 1] != 0: energies[row + 1][col - 1] += 1
                        if energies[row + 1][col + 1] != 0: energies[row + 1][col + 1] += 1
                        if energies[row][col - 1] != 0: energies[row][col - 1] += 1
                        if energies[row][col + 1] != 0: energies[row][col + 1] += 1
                        if energies[row - 1][col] != 0: energies[row - 1][col] += 1
                        if energies[row + 1][col] != 0: energies[row + 1][col] += 1

            if new_flashes == 0: break
            flashes += new_flashes

        steps += 1

    print(steps)


solve("input-test.txt")
solve("input.txt")
