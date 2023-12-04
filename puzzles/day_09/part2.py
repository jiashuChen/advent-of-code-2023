import pathlib
import re


def parse_input():
    input_path = pathlib.Path(__file__).parent.joinpath("input.txt")
    with input_path.open("r") as input_file:
        input_lines = input_file.readlines()

    rows = [list(map(int, re.split("\s+", line.strip()))) for line in input_lines]

    return rows


def solve_line(line):
    if all(x == 0 for x in line):
        return 0
    D = []
    for i in range(1, len(line)):
        D.append(line[i] - line[i - 1])
    return line[0] - solve_line(D)


def part(lines):
    map(lambda line: line.reverse(), lines)
    return sum(solve_line(line) for line in lines)


if __name__ == "__main__":
    lines = parse_input()
    print(part(lines))
