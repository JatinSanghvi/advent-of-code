import re


def solve(text):
    tokens = re.findall(r'-?\d+', text)
    numbers = [int(token) for token in tokens]
    print(sum(numbers))


def main():
    solve('[1,2,3]')  # 6
    solve('{"a":2,"b":4}')  # 6
    solve('[[[3]]]')  # 3
    solve('{"a":{"b":4},"c":-1}')  # 3
    solve('{"a":[-1,1]}')  # 0
    solve('[-1,{"a":1}]')  # 0

    with open('input.txt') as file:
        input = file.read()
    solve(input)  # 191164


if __name__ == '__main__':
    main()
