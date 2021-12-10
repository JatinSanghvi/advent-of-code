def solve(path):
    with open(path) as file:
        lines = file.readlines()

    score = 0
    for line in lines:
        stack = []
        for char in line.rstrip():
            if char in "([{<":
                stack.append(char)
            elif "([{<"[")]}>".index(char)] != stack.pop():
                score += [3, 57, 1197, 25137][")]}>".index(char)]
                break

    print(score)


solve("input-test.txt")
solve("input.txt")
