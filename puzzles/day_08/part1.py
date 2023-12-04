import itertools
import pathlib
import re
from pprint import pprint

INSTRUCTIONS = [
    0 if c == "L" else 1
    for c in "LLRRRLLRRRLRRRLRLRLLRRLRRRLLLRLRRRLRRRLRLLRRLRRRLLRRLRRLRLRRRLRRLLRLRRLRRRLRRLLRRRLRLLLRLRRRLRRLLLLRRRLRRRLRRRLRLRRLRRLRLRRLLRLLRRRLRRLRLLRRLRRLLRLLRLRRRLRLRLRRRLRRLLLRLRRRLLRLLRRRLRLRLRRRLLRLLLLRRRLRRRLRLRRRLRRLRRLLRLRLRRRLRRRLRLRRLLLLRLRRRLRRRLRLRRRLRLRRLRLRRRR"
]


def parse_input():
    input_path = pathlib.Path(__file__).parent.joinpath("input.txt")
    with input_path.open("r") as input_file:
        input_lines = input_file.readlines()

    nodes = {}
    for line in input_lines:
        node, left, right = re.findall("\w{3}", line)
        nodes[node] = [left, right]

    return nodes


def part(nodes):
    count = 0
    node = "AAA"
    for instruction in itertools.cycle(INSTRUCTIONS):
        if node == "ZZZ":
            break
        count += 1
        node = nodes[node][instruction]
    return count


if __name__ == "__main__":
    nodes = parse_input()
    pprint(nodes)
    print(part(nodes))
