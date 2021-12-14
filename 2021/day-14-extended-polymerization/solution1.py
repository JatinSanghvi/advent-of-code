def solve(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file.readlines()]

    template = lines[0]
    replacements = {line.split()[0]: line.split()[0][0] + line.split()[2] for line in lines[2:]}

    for _ in range(10):
        new_template = []
        for index in range(len(template) - 1):
            new_template.append(replacements[template[index] + template[index + 1]])
        new_template.append(template[-1])
        template = "".join(new_template)

    element_counts = list(map(template.count, set(template)))
    print(max(element_counts) - min(element_counts))


solve("input-test.txt")
solve("input.txt")
