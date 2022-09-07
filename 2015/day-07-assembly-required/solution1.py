def solve(path, input_wire):
    with open(path) as file:
        lines = file.readlines()

    values = dict()

    for line in lines:
        formula, wire = line.strip().split(' -> ')
        values[wire] = formula

    def resolve(wire):
        try:
            return int(wire)
        except:
            try:
                values[wire] = int(values[wire])
            except:
                if ' AND ' in values[wire]:
                    wire1, wire2 = values[wire].split(' AND ')
                    values[wire] = resolve(wire1) & resolve(wire2)
                elif ' OR ' in values[wire]:
                    wire1, wire2 = values[wire].split(' OR ')
                    values[wire] = resolve(wire1) | resolve(wire2)
                elif ' LSHIFT ' in values[wire]:
                    wire1, wire2 = values[wire].split(' LSHIFT ')
                    values[wire] = resolve(wire1) << resolve(wire2)
                elif ' RSHIFT ' in values[wire]:
                    wire1, wire2 = values[wire].split(' RSHIFT ')
                    values[wire] = resolve(wire1) >> resolve(wire2)
                elif 'NOT ' in values[wire]:
                    wire1 = values[wire].replace('NOT ', '')
                    values[wire] = 65535 - resolve(wire1)
                else:
                    values[wire] = resolve(values[wire])

            return values[wire]

    resolve(input_wire)
    print(f'{input_wire}: {values[input_wire]}')


def main():
    solve('input-test.txt', 'd')  # d: 72
    solve('input-test.txt', 'e')  # e: 507
    solve('input-test.txt', 'f')  # f: 492
    solve('input-test.txt', 'g')  # g: 114
    solve('input-test.txt', 'h')  # h: 65412
    solve('input-test.txt', 'i')  # i: 65079
    solve('input-test.txt', 'x')  # x: 123
    solve('input-test.txt', 'y')  # y: 456
    print('---')
    solve('input.txt', 'a')  # a: 46065


if __name__ == '__main__':
    main()
