class Map:
    def __init__(self):
        self.dest_start = 0
        self.src_start = 0
        self.range = 0

    def contains(self, value: int) -> bool:
        return self.src_start <= value < self.src_start + self.range

    def convert(self, value: int) -> int:
        return self.dest_start + (value - self.src_start)


def line_to_list_of_map_ranges(block: str) -> list:
    """Parses a space-separated block of lines into a list of Map objects"""
    lines = block.strip().split("\n")
    maps = []
    for line in lines:
        dest, src, length = map(int, line.strip().split())
        m = Map()
        m.dest_start = dest
        m.src_start = src
        m.range = length
        maps.append(m)
    return maps


def maps_and_src_to_dest(value: int, map_list: list) -> int:
    for m in map_list:
        if m.contains(value):
            return m.convert(value)
    return value  # no mapping found — stays the same


def seeds_to_locations(seeds: list, maps_blocks: list) -> list:
    """Converts each seed to its final location by applying each map layer in order."""
    all_map_layers = [line_to_list_of_map_ranges("\n".join(block)) for block in maps_blocks]

    for seed in seeds:
        value = seed
        for map_layer in all_map_layers:
            value = maps_and_src_to_dest(value, map_layer)
        yield value


def parse_input(file_path: str):
    """Reads and organizes seed values and map blocks from the input file."""
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file if line.strip()]

    seeds = list(map(int, lines[0].split(":")[1].strip().split()))
    maps = []
    current_map = []

    for line in lines[1:]:
        if line.endswith("map:"):
            if current_map:
                maps.append(current_map)
                current_map = []
        else:
            current_map.append(line)
    if current_map:
        maps.append(current_map)

    return seeds, maps
