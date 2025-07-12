class Map:
    def __init__(self, dest_start, src_start, length):
        self.dest_start = dest_start
        self.src_start = src_start
        self.length = length

    def contains(self, value: int) -> bool:
        return self.src_start <= value < self.src_start + self.length

    def convert(self, value: int) -> int:
        return self.dest_start + (value - self.src_start)

    def map_range(self, start: int, end: int):
        """Map a [start, end) range if it overlaps with this map rule"""
        src_end = self.src_start + self.length
        overlap_start = max(start, self.src_start)
        overlap_end = min(end, src_end)

        if overlap_start >= overlap_end:
            return None  # No overlap

        delta = self.dest_start - self.src_start
        return (overlap_start + delta, overlap_end + delta)


def parse_input(file_path: str):
    """
    Parses the input file and returns:
    - list of seed values (for Part 1)
    - list of map layers, each a list of Map objects
    """
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    seeds = list(map(int, lines[0].split(":")[1].split()))
    maps = []
    current_layer = []

    for line in lines[1:]:
        if line.endswith("map:"):
            if current_layer:
                maps.append(current_layer)
            current_layer = []
        else:
            dest, src, length = map(int, line.split())
            current_layer.append(Map(dest, src, length))

    if current_layer:
        maps.append(current_layer)

    return seeds, maps


def apply_maps_to_value(value: int, map_layers: list) -> int:
    """Maps a single seed value through all map layers."""
    for layer in map_layers:
        for rule in layer:
            if rule.contains(value):
                value = rule.convert(value)
                break  # only use the first matching rule in each layer
    return value


def apply_maps_to_ranges(ranges: list, map_layers: list) -> list:
    """
    Maps a list of seed ranges [(start, end)] through all layers.
    This is used in Part 2 for efficient range processing.
    """
    for layer in map_layers:
        result = []
        for start, end in ranges:
            unmapped = [(start, end)]

            for rule in layer:
                next_unmapped = []

                while unmapped:
                    s, e = unmapped.pop()
                    mapped = rule.map_range(s, e)

                    if mapped:
                        # Add mapped section
                        result.append(mapped)
                        # Add before
                        if s < rule.src_start:
                            next_unmapped.append((s, min(e, rule.src_start)))
                        # Add after
                        if e > rule.src_start + rule.length:
                            next_unmapped.append((max(s, rule.src_start + rule.length), e))
                    else:
                        next_unmapped.append((s, e))

                unmapped = next_unmapped

            result.extend(unmapped)  # leftover ranges with no matching rule
        ranges = result
    return ranges
