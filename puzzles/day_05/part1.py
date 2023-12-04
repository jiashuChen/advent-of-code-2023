# --- Day 4: Scratchcards ---
# https://adventofcode.com/2023/day/4
import pathlib

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent.joinpath("input", "day-05.txt")

SEEDS = []
SEEDS_PAIR = []
MAPS = {}


def parse_seed_part1(line):
    global SEEDS
    SEEDS = list(map(int, line.removeprefix("seeds:").strip().split()))


# Stuff written before part 2 came in to place
def parse_input():
    global SEEDS, MAPS

    with INPUT_PATH.open("r") as input_files:
        lines = [line.strip() for line in input_files.readlines()]
    current_map_name = ""
    for line in lines:
        if len(line) == 0:
            continue
        elif line.startswith("seeds"):
            parse_seed_part1(line)
        elif line.endswith("map:"):
            current_map_name = line.removesuffix(" map:")
            MAPS[current_map_name] = []
        else:
            destination_start, source_start, range_ = map(int, line.split())
            MAPS[current_map_name].append([source_start, destination_start, range_])


def get_destination_from_map(current_map, source):
    for source_start, destination_start, range_ in current_map:
        if source_start <= source < source_start + range_:
            return source - source_start + destination_start
    return source


def find_smallest_location_part_1():
    current_sources = SEEDS
    for map_name in (
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ):
        current_map = MAPS[map_name]
        next_sources = [
            get_destination_from_map(current_map, source) for source in current_sources
        ]
        current_sources = next_sources

    return min(current_sources)


if __name__ == "__main__":
    parse_input()
    print(find_smallest_location_part_1())
