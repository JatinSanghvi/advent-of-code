def solve(path):
    with open(path) as file:
        lines = file.readlines()

    # Add matrix border to simplify code.
    energies = [[int(char) for char in "0" + line.rstrip() + "0"] for line in ["0000000000"] + lines + ["0000000000"]]

    flashes = 0

    for step in range(100):
        energies = [[energy + 1 for energy in energy_row] for energy_row in energies]

        while True:
            new_flashes = 0
            for row in range(1, 11):
                for col in range(1, 11):
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

    print(flashes)


solve("input-test.txt")
solve("input.txt")
