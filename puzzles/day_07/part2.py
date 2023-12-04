import math
import pathlib
from pprint import pprint

ORDER = "AKQT98765432J"


def parse_input():
    input_path = pathlib.Path(__file__).parent.joinpath("input.txt")
    with input_path.open("r") as input_file:
        input_lines = input_file.readlines()

    cards = {line.split()[0]: int(line.split()[1]) for line in input_lines}

    return cards


def get_entrypy(card):
    return -sum(
        map(
            lambda p: p * math.log(p),
            [card.count(c) / len(card) for c in set(card)],
        )
    )


def get_entrypy_with_joker(card):
    try:
        top = sorted(
            card.replace("J", ""),
            key=lambda c: card.count(c),
        )[-1]
        return get_entrypy(card.replace("J", top))
    except IndexError:
        return get_entrypy(card)


def part(cards):
    sorted_cards_by_winning_entropy = {
        i: bid
        for i, (__, bid) in enumerate(
            sorted(
                cards.items(),
                key=lambda h: (get_entrypy_with_joker(h[0]), *map(ORDER.index, h[0])),
                reverse=True,
            ),
            start=1,
        )
    }
    pprint(sorted_cards_by_winning_entropy)
    return sum(
        order * value for order, value in sorted_cards_by_winning_entropy.items()
    )


if __name__ == "__main__":
    cards = parse_input()
    pprint(cards)
    print(part(cards))
