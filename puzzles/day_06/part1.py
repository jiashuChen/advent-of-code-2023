import math
import pathlib
import re


def parse_input():
    input_path = pathlib.Path(__file__).parent.joinpath("input.txt")
    with input_path.open("r") as input_file:
        input_lines = input_file.readlines()

    races, records = [
        list(map(int, re.split("\s+", line.split(":")[1].strip())))
        for line in input_lines
    ]
    return races, records


def part1(races, records):
    wining_plans = []
    for race, record in zip(races, records):
        plans = [x * (race - x) for x in range(1, race)]
        print(plans)
        winnable = [plan > record for plan in plans].count(True)
        if winnable > 0:
            wining_plans.append(winnable)
    return math.prod(wining_plans)


if __name__ == "__main__":
    races, records = parse_input()
    print(part1(races, records))
