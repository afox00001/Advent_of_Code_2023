if __name__ == "__main__":
    from Map import parse_input, apply_maps_to_ranges

    seeds, map_layers = parse_input("input.txt")
    seed_ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
    final_ranges = apply_maps_to_ranges(seed_ranges, map_layers)
    print(min(start for start, _ in final_ranges))
