import pathlib
import re


def parse_input():
    input_path = pathlib.Path(__file__).parent.joinpath("input.txt")
    with input_path.open("r") as input_file:
        input_lines = input_file.readlines()

    rows = [list(line.strip()) for line in input_lines]
    return rows


def find_gear(board, r, c):
    cell_with_digit = []
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
            if board[check_r][check_c].isdigit():
                cell_with_digit.append([i, j])
        except IndexError:
            pass

    checked_rows = {}
    for checked_row, checked_col in cell_with_digit:
        checked_rows.setdefault(checked_row, []).append(c + checked_col)
    matched_num = []
    for checked_row in checked_rows:
        row = board[r + checked_row]
        for group in re.finditer(r"\d+", "".join(row)):
            matched_num_in_row = set()
            for x in range(group.span()[0], group.span()[1]):
                if x in checked_rows[checked_row]:
                    matched_num_in_row.add(
                        int("".join(row[group.span()[0] : group.span()[1]]))
                    )
            if len(matched_num_in_row) == 1:
                matched_num.append(matched_num_in_row.pop())
    print(matched_num)
    if len(matched_num) != 2:
        return 0

    return matched_num[0] * matched_num[1]


def part1(board):
    gear = []

    for r in range(len(board)):
        row = board[r]
        for c in range(len(row)):
            if board[r][c] == "*":
                gear.append(find_gear(board, r, c))
    return sum(gear)


if __name__ == "__main__":
    games = parse_input()
    print(part1(games))
