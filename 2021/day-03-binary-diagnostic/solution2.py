def solve(path):
    with open(path) as file:
        input_matrix = [[int(bit) for bit in line.rstrip()] for line in file.readlines()]

    columns = len(input_matrix[0])

    matrix = input_matrix
    for column_index in range(columns):
        bits = [row[column_index] for row in matrix]
        mode = max(set(bits), key=lambda bit: 10e6 * bits.count(bit) + bit) # Set mode to 1 if  case of a tie.
        matrix = list(filter(lambda row: row[column_index] == mode, matrix))
        if len(matrix) == 1:
            break

    generator = int("".join(str(bit) for bit in matrix[0]), 2)

    matrix = input_matrix
    for column_index in range(columns):
        bits = [row[column_index] for row in matrix]
        mode = max(set(bits), key=lambda bit: 10e6 * bits.count(bit) + bit)
        antimode = 1 if mode == 0 else 0
        matrix = list(filter(lambda row: row[column_index] == antimode, matrix))
        if len(matrix) == 1:
            break

    scrubber = int("".join(str(bit) for bit in matrix[0]), 2)

    print(generator * scrubber)


solve("input-test.txt")
solve("input.txt")
