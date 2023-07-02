import re


def solve(prev_pass):
    pattern1 = re.compile(r'abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz')
    pattern2 = re.compile(r'[ilo]')
    pattern3 = re.compile(r'(.)\1.*(.)\2')

    next_pass = next(prev_pass)
    while (not pattern1.search(next_pass) or pattern2.search(next_pass) or not pattern3.search(next_pass)):
        next_pass = next(next_pass)

    next_pass = next(next_pass)
    while (not pattern1.search(next_pass) or pattern2.search(next_pass) or not pattern3.search(next_pass)):
        next_pass = next(next_pass)

    print(next_pass)


def next(prev_pass):
    for pos in range(7, -1, -1):
        if prev_pass[pos] != 'z':
            return prev_pass[:pos] + chr(ord(prev_pass[pos]) + 1) + ('a' * (7 - pos))


def main():
    solve('hxbxwxba')  # hxcaabcc


if __name__ == '__main__':
    main()
