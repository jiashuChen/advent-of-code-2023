# --- Day 4: Scratchcards ---
# https://adventofcode.com/2023/day/4
import pathlib
import re
import sys

INPUT_PATH = pathlib.Path(__file__).parent.parent.joinpath("input", "day-04.txt")


# Stuff written before part 2 came in to place
def read_puzzle_part1():
    lines = [
        re.sub(r"\s+", " ", line).split("|")
        for line in INPUT_PATH.read_text(sys.getdefaultencoding()).splitlines()
    ]

    answer = 0
    for winnings_str, card_str in lines:
        winnings = winnings_str.strip().split(" ")
        cards = card_str.strip().split(" ")
        common = len(set(winnings).intersection(set(cards)))
        if common > 0:
            answer += 2 ** (common - 1)

    return answer


def read_puzzle():
    raw_lines = [
        re.sub(r"\s+", " ", line).split("|")
        for line in INPUT_PATH.read_text(sys.getdefaultencoding()).splitlines()
    ]

    lines = []
    for winnings_str, card_str in raw_lines:
        winnings = winnings_str.strip().split(" ")
        cards = card_str.strip().split(" ")
        common = len(set(winnings).intersection(set(cards)))
        lines.append(common)

    return lines


def part_2(lines):
    answer = [1] * (len(lines))
    for idx, common in enumerate(lines):
        if common == 0:
            continue
        for i in range(common):
            if i > len(lines) - 1:
                continue
            answer[idx + i + 1] += answer[idx]

    print(answer)
    return sum(answer)


if __name__ == "__main__":
    lines = read_puzzle()
    print(part_2(lines))
