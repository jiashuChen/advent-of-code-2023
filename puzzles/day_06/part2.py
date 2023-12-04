import pathlib
import re


def parse_input():
    input_path = pathlib.Path(__file__).parent.joinpath("input.txt")
    with input_path.open("r") as input_file:
        input_lines = input_file.readlines()

    race, record = [
        int("".join(re.split("\s+", line.split(":")[1].strip())))
        for line in input_lines
    ]
    return race, record


def part2(race, record):
    plans = [x * (race - x) for x in range(1, race)]
    winnable = [plan > record for plan in plans].count(True)
    return winnable


if __name__ == "__main__":
    race, record = parse_input()
    print(part2(race, record))
