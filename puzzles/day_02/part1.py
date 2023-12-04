import pathlib
from pprint import pprint


def parse_line(line: str):
    game_id = line.split(":")[0].split(" ")[1]
    games = [
        {g.split()[1]: int(g.split()[0]) for g in game.split(",")}
        for game in line.split(":")[1].split(";")
    ]
    return int(game_id), games


def parse_input():
    input_path = pathlib.Path(__file__).parent.joinpath("input.txt")
    with input_path.open("r") as input_file:
        input_lines = input_file.readlines()

    games = {}
    for line in input_lines:
        game_id, game_order = parse_line(line)
        games[game_id] = game_order

    return games


def is_game_possible(draws) -> bool:
    ceiling = {"red": 12, "green": 13, "blue": 14}
    return all(
        all(draw[color] <= ceiling[color] for color, num in draw.items())
        for draw in draws
    )


def part1(games):
    return sum(game_id for game_id, draws in games.items() if is_game_possible(draws))


if __name__ == "__main__":
    games = parse_input()
    pprint(games)
    print(part1(games))
