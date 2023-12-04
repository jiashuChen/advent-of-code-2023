import math
import pathlib
from pprint import pprint


class Cell:
    def __init__(self, actions, r, c, char):
        self.actions = actions
        self.r = r
        self.c = c
        self.char = char

    def __repr__(self):
        return f"({self.r}, {self.c}, {self.char})"


START_ROW, START_COL = 0, 0


def parse_cell(row, col, char):
    match char:
        case '|':
            return Cell([(1, 0), (-1, 0)], row, col, char)
        case '-':
            return Cell([(0, 1), (0, -1)], row, col, char)
        case 'L':
            return Cell([(-1, 0), (0, 1)], row, col, char)
        case 'J':
            return Cell([(0, -1), (-1, 0)], row, col, char)
        case '7':
            return Cell([(1, 0), (0, -1)], row, col, char)
        case 'F':
            return Cell([(1, 0), (0, 1)], row, col, char)
        case '.':
            return Cell([], row, col, char)
        case 'S':
            global START_ROW, START_COL
            START_ROW, START_COL = row, col
            return Cell([(1, 0), (0, -1), (-1, 0), (0, 1)], row, col, char)


def parse_input():
    input_path = pathlib.Path(__file__).parent.joinpath("input.txt")
    with input_path.open("r") as input_file:
        input_lines = [line.strip() for line in input_file.readlines()]

    rows = [
        [parse_cell(row, col, c) for col, c in enumerate(line)] for row, line in enumerate(input_lines)
    ]

    return rows


def part(rows):
    pos_to_explore = [[START_ROW, START_COL, 0, START_ROW, START_ROW]]
    max_explored = 0
    while pos_to_explore:
        r, c, s, f_r, f_c = pos_to_explore.pop()
        cell = rows[r][c]
        print(f"exploring cell r {r} c {c} char {cell.char} at step {s}")
        step = s + 1
        max_explored = max(max_explored, step)
        for action in cell.actions:
            n_r = r + action[0]
            n_c = c + action[1]
            if n_r < 0 or n_c < 0 or n_r >= len(rows) or n_c >= len(rows[0]) or (f_r == n_r and f_c == n_c):
                continue
            new_cell = rows[n_r][n_c]
            assert new_cell.r == n_r
            assert new_cell.c == n_c
            print(f"exploring new cell r {n_c} c {n_c} char {new_cell.char} at step {step}")
            if n_r == START_ROW and n_c == START_COL:
                return max_explored // 2
            else:
                pos_to_explore.append([new_cell.r, new_cell.c, step, r, c])


if __name__ == "__main__":
    rows = parse_input()
    pprint(part(rows))
