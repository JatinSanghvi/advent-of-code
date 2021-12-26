import functools


@functools.total_ordering
class Values:
    def __init__(self, w=0, x=0, y=0, z=0):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return other and self.w == other.w and self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return (self.w, self.x, self.y, self.z) < (other.w, other.x, other.y, other.z)

    def __hash__(self):
        return hash((self.w, self.x, self.y, self.z))

    def __repr__(self):
        return f'Values({self.w}, {self.x}, {self.y}, {self.z})'

    def clone(self, var, value):
        if var == 'w': return Values(value, self.x, self.y, self.z)
        if var == 'x': return Values(self.w, value, self.y, self.z)
        if var == 'y': return Values(self.w, self.x, value, self.z)
        if var == 'z': return Values(self.w, self.x, self.y, value)

    def get_value(self, token):
        if token == 'w': return self.w
        if token == 'x': return self.x
        if token == 'y': return self.y
        if token == 'z': return self.z
        return int(token)


def solve(path):
    with open(path) as file:
        lines = file.readlines()

    values_dict = {Values(0, 0, 0, 0): 0}

    for line in lines:
        tokens = line.split()
        if tokens[0] == 'inp':
            values_tuples = [(values.clone(tokens[1], input), values_dict[values] * 10 + input) for values in values_dict for input in range(1, 10)]
        elif tokens[0] == 'add':
            values_tuples = [(values.clone(tokens[1], values.get_value(tokens[1]) + values.get_value(tokens[2])), input)
                             for values, input in values_dict.items()]
        elif tokens[0] == 'mul':
            values_tuples = [(values.clone(tokens[1], values.get_value(tokens[1]) * values.get_value(tokens[2])), input)
                             for values, input in values_dict.items()]
        elif tokens[0] == 'div':
            values_tuples = [(values.clone(tokens[1], int(values.get_value(tokens[1]) / values.get_value(tokens[2]))), input)
                             for values, input in values_dict.items()]
        elif tokens[0] == 'mod':
            values_tuples = [(values.clone(tokens[1], values.get_value(tokens[1]) % values.get_value(tokens[2])), input)
                             for values, input in values_dict.items()]
        elif tokens[0] == 'eql':
            values_tuples = [(values.clone(tokens[1], int(values.get_value(tokens[1]) == values.get_value(tokens[2]))), input)
                             for values, input in values_dict.items()]

            # Optimization hack, specific to the problem: If there are values with Zprev % 26 + V2 == W, only consider them.
            if tokens[1] == 'x' and tokens[2] == 'w':
                values_tuples_2 = [(values, input) for values, input in values_tuples if values.x == 1]
                if len(values_tuples_2):
                    values_tuples = values_tuples_2

        # Will retain smallest inputs only, by virtue of sorting.
        values_dict = {values: input for values, input in reversed(sorted(values_tuples))}

    print(min(input for values, input in values_dict.items() if values.z == 0))


# solve('input-test-1.txt')
# solve('input-test-2.txt')
# solve('input-test-3.txt')
solve('input.txt')
