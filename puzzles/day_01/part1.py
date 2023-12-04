INPUT = """
"""


def part1():
    lines = [("".join(c for c in line if c.isdigit())) for line in INPUT.splitlines()]
    print(lines)
    return sum(int(f"{line[0]}{line[-1]}") for line in lines)


if __name__ == "__main__":
    answer = part1()
    print(answer)
