import pathlib


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


def find_power_of_game(game_id, draws) -> bool:
    min_red = max(draw.get("red", 1) for draw in draws)
    min_blue = max(draw.get("blue", 1) for draw in draws)
    min_green = max(draw.get("green", 1) for draw in draws)
    product = min_red * min_blue * min_green
    print(f"game: {game_id}, prod: {product}")
    return product


def part1(games):
    return sum(find_power_of_game(game_id, draws) for game_id, draws in games.items())


if __name__ == "__main__":
    games = parse_input()
    print(part1(games))
