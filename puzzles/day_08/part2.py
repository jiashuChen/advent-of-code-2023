import itertools
import pathlib
import re
from math import lcm

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
    starting_nodes = set(node for node in nodes.keys() if node.endswith("A"))
    result = []
    for node in starting_nodes:
        count = 0
        for instruction in itertools.cycle(INSTRUCTIONS):
            if node.endswith("Z"):
                break
            count += 1
            node = nodes[node][instruction]
        result.append(count)
    return lcm(*result)


if __name__ == "__main__":
    nodes = parse_input()
    print(part(nodes))
