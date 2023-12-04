import pathlib
import re
from itertools import chain
from pprint import pprint


def parse_input():
    input_path = pathlib.Path(__file__).parent.joinpath("input.txt")
    with input_path.open("r") as input_file:
        input_lines = input_file.readlines()

    rows = [list(line.strip()) for line in input_lines]
    return rows


def wipe_neighbour(board, r, c):
    for i, j in [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0],
        [-1, 1],
        [-1, -1],
        [1, 1],
        [1, -1],
    ]:
        try:
            check_r = r + i
            check_c = c + j
            # print(f"  checking cell: r {r} c {c} i {i} j {j} {check_r} {check_c}. value: {board[check_r][check_c]}")
            if board[check_r][check_c].isdigit():
                board[check_r][check_c] = " "
        except IndexError:
            pass


def part1(board):
    all_nums_before = list(
        chain.from_iterable(
            [group for group in re.findall(r"\d+", "".join(row)) if " " not in group]
            for row in board
        )
    )

    for r in range(len(board)):
        row = board[r]
        for c in range(len(row)):
            # print(f"looking at cell: {r}, {c} v = {board[r][c]}")
            if board[r][c] != " " and not board[r][c].isdigit() and board[r][c] != ".":
                # print(f" wiping neighbour: {r}, {c} v = {board[r][c]}")
                wipe_neighbour(board, r, c)
    print("\n".join(["".join(row) for row in board]))

    all_nums = list(
        chain.from_iterable(
            [
                group
                for group in re.findall(r"\s*\d+\s*", "".join(row))
                if " " not in group
            ]
            for row in board
        )
    )
    print(all_nums_before)
    sum_before = sum(map(int, all_nums_before))
    sum_after = sum(map(int, all_nums))
    return sum_before - sum_after


if __name__ == "__main__":
    games = parse_input()
    pprint(games)
    print(part1(games))
