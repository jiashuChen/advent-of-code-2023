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
    for i in range(len(line) - 1):
        D.append(line[i + 1] - line[i])
    return line[-1] + solve_line(D)


def part(lines):
    return sum(solve_line(line) for line in lines)


if __name__ == "__main__":
    lines = parse_input()
    print(part(lines))
