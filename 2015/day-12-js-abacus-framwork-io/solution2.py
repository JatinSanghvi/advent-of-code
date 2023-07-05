import re


def solve(text: str):
    obj_regex = re.compile(r'\{[^\{\}]*\}')
    num_regex = re.compile(r'-?\d+')

    def sum_numbers(text):
        tokens = num_regex.findall(text)
        numbers = [int(token) for token in tokens]
        return sum(numbers)

    def replace(match: re.Match[str]) -> str:
        text = match.group()
        return '0' if ':"red"' in text else str(sum_numbers(text))

    old_text, new_text = '', text
    while new_text != old_text:
        old_text = new_text
        new_text = obj_regex.sub(replace, old_text)

    print(sum_numbers(new_text))


def main():
    solve('[1,2,3]')  # 6
    solve('[1,{"c":"red","b":2},3]')  # 4
    solve('{"d":"red","e":[1,2,3,4],"f":5}')  # 0
    solve('[1,"red",5]')  # 6

    with open('input.txt') as file:
        input = file.read()
    solve(input)  # 87842


if __name__ == '__main__':
    main()
