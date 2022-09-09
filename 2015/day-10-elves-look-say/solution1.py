def solve(value, steps):
    for _ in range(steps):
        new_value = ''
        char = value[0]
        copies = 1
        for next_char in value[1:] + '$':
            if char == next_char:
                copies += 1
            else:
                new_value += str(copies) + char
                char = next_char
                copies = 1
        value = new_value

    print(len(value))


def main():
    solve('1', 5)
    solve('3113322113', 40)


if __name__ == '__main__':
    main()
