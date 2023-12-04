INPUT: str = """
"""


def cleanup():
    global INPUT
    replaces = [
        ["one", "o1e"],
        ["two", "t2o"],
        ["three", "t3e"],
        ["four", "f4r"],
        ["five", "f5e"],
        ["six", "s6x"],
        ["seven", "s7n"],
        ["eight", "e8t"],
        ["nine", "n9e"],
    ]
    for [word, substitute] in replaces:
        print(f"replacing word: {word} with {substitute}")
        INPUT = INPUT.replace(word, str(substitute))


def part2():
    lines = [("".join(c for c in line if c.isdigit())) for line in INPUT.splitlines()]
    print(lines)
    return sum(int(f"{line[0]}{line[-1]}") for line in lines)


if __name__ == "__main__":
    cleanup()
    print(INPUT)
    answer = part2()
    print(answer)
