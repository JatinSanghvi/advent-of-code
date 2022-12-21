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

    def yell(name: str) -> int:
        job = jobs[name]
        if isinstance(job, int): return job

        left_name, op, right_name = job
        left_yell, right_yell = yell(left_name), yell(right_name)

        if op == '+': return left_yell + right_yell
        elif op == '-': return left_yell - right_yell
        elif op == '*': return left_yell * right_yell
        elif op == '/': return left_yell // right_yell

    print(yell('root'))


def main():
    solve('input-test.txt')  # 152
    solve('input.txt')  # 62386792426088


if __name__ == '__main__':
    main()
