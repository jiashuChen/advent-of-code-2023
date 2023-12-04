import pathlib

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent.joinpath("input", "day-05.txt")

SEEDS_PAIR = []
MAPS = {}


def parse_seed_part2(line):
    global SEEDS_PAIR

    def pairwise(t):
        it = iter(t)
        return zip(it, it)

    SEEDS_PAIR = list(pairwise(map(int, line.removeprefix("seeds:").strip().split())))
    SEEDS_PAIR = [[s, r + s + 1] for [s, r] in SEEDS_PAIR]


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
            parse_seed_part2(line)
        elif line.endswith("map:"):
            current_map_name = line.removesuffix(" map:")
            MAPS[current_map_name] = []
        else:
            destination_start, source_start, range_ = map(int, line.split())
            MAPS[current_map_name].append([source_start, destination_start, range_])


def get_ranges(src_ranges, map_list):
    result = []
    for a, b in src_ranges:
        covered_ranges = []
        for source, dest, range_ in map_list:
            x, y = source, source + range_ - 1
            if b < x or y < a:
                continue
            o_start = max(a, x)
            o_end = min(b, y)
            covered_ranges.append((o_start, o_end))
            result.append((o_start - source + dest, o_end - source + dest))
        # now check for all sections of range left uncovered
        if not covered_ranges:
            result.append((a, b))
            continue
        covered_ranges.sort()
        # check beginning
        if covered_ranges[0][0] > a:
            result.append((a, covered_ranges[0][0] - 1))
        # check end
        if covered_ranges[-1][1] < b:
            result.append((covered_ranges[-1][1] + 1, b))
        for i in range(len(covered_ranges) - 1):
            x1, y1 = covered_ranges[i]
            x2, y2 = covered_ranges[i + 1]
            if x2 > y1 + 1:
                result.append((y1 + 1, x2 - 1))
    return result


def get_location_ranges(seed_ranges):
    current_seeds = seed_ranges
    for map_list in [
        MAPS[current_map]
        for current_map in (
            "seed-to-soil",
            "soil-to-fertilizer",
            "fertilizer-to-water",
            "water-to-light",
            "light-to-temperature",
            "temperature-to-humidity",
            "humidity-to-location",
        )
    ]:
        current_seeds = get_ranges(current_seeds, map_list)
    return current_seeds


if __name__ == "__main__":
    parse_input()
    locations = get_location_ranges(SEEDS_PAIR)
    print(min(locations)[0])
