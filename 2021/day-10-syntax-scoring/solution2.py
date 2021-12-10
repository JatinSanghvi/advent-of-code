from functools import reduce


def solve(path):
    with open(path) as file:
        lines = file.readlines()

    scores = []
    for line in lines:
        stack = []
        broke_out = False

        for char in line.rstrip():
            if char in "([{<":
                stack.append(char)
            elif "([{<"[")]}>".index(char)] == stack[-1]:
                stack.pop()
            else:
                broke_out = True
                break

        if broke_out: continue
        score = reduce(lambda a, b: 5 * a + "([{<".index(b) + 1, reversed(stack), 0)
        scores.append(score)

    scores = sorted(scores)
    print(scores[len(scores) // 2])


solve("input-test.txt")
solve("input.txt")
