from typing import Dict, Tuple


def solve(path):
    with open(path) as file:
        lines = [line.rstrip('\n') for line in file.readlines()]

    jobs: Dict[str, int | Tuple[str, str, str]] = {}

    for line in lines:
        name, job = line.split(': ')
        try:
            jobs[name] = int(job)
        except:
            jobs[name] = job.split()

    def yell(name: str) -> int | None:
        if name == 'humn': return None
        job = jobs[name]
        if isinstance(job, int): return job

        left_name, op, right_name = job
        left_yell, right_yell = yell(left_name), yell(right_name)

        if left_yell is None: yells[right_name] = right_yell; return None
        elif right_yell is None: yells[left_name] = left_yell; return None
        else:
            if op == '+': return left_yell + right_yell
            elif op == '-': return left_yell - right_yell
            elif op == '*': return left_yell * right_yell
            elif op == '/': return left_yell // right_yell

    yells: Dict[name, int] = {}
    yell('root')

    def make_yell(name: str, required: int) -> int:
        if name == 'humn': return required
        job = jobs[name]
        left_name, op, right_name = job

        if left_name in yells:
            left_yell = yells[left_name]
            if op == '+': return make_yell(right_name, required - left_yell)
            elif op == '-': return make_yell(right_name, left_yell - required)
            elif op == '*': return make_yell(right_name, required // left_yell)
            elif op == '/': return make_yell(right_name, left_yell // required)
        elif right_name in yells:
            right_yell = yells[right_name]
            if op == '+': return make_yell(left_name, required - right_yell)
            elif op == '-': return make_yell(left_name, required + right_yell)
            elif op == '*': return make_yell(left_name, required // right_yell)
            elif op == '/': return make_yell(left_name, required * right_yell)

    jobs['root'][1] = '-'
    print(make_yell('root', 0))


def main():
    solve('input-test.txt')  # 301
    solve('input.txt')  # 3876027196185


if __name__ == '__main__':
    main()
