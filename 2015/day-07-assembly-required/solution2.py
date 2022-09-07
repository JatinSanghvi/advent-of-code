def solve(path):
    with open(path) as file:
        lines = file.readlines()

    values = dict()

    for line in lines:
        formula, wire = line.strip().split(' -> ')
        values[wire] = formula
    values['b'] = 46065

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

    print(resolve('a'))


def main():
    solve('input.txt')  # 14134


if __name__ == '__main__':
    main()
