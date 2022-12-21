def solve(path):
    with open(path) as file:
        lines = [line.rstrip('\n') for line in file.readlines()]

    numbers = [int(line) * 811589153 for line in lines]
    length = len(numbers)
    next_indices = [(index + 1) % length for index in range(length)]
    prev_indices = [(index - 1) % length for index in range(length)]

    for _ in range(10):
        for (index, number) in enumerate(numbers):

            # Remove number.
            old_prev_index = prev_indices[index]
            old_next_index = next_indices[index]

            next_indices[old_prev_index] = old_next_index
            prev_indices[old_next_index] = old_prev_index

            # Find next location.
            moves = number % (length - 1)
            new_prev_index = old_prev_index
            for _ in range(moves):
                new_prev_index = next_indices[new_prev_index]

            new_next_index = next_indices[new_prev_index]

            # Insert number.
            next_indices[new_prev_index] = index
            prev_indices[new_next_index] = index

            next_indices[index] = new_next_index
            prev_indices[index] = new_prev_index

    sum = 0

    index = numbers.index(0)
    for _ in range(1000): index = next_indices[index]
    sum += numbers[index]
    for _ in range(1000): index = next_indices[index]
    sum += numbers[index]
    for _ in range(1000): index = next_indices[index]
    sum += numbers[index]

    print(sum)


def main():
    solve('input-test.txt')  # 1623178306
    solve('input.txt')  # 17200008919529


if __name__ == '__main__':
    main()
