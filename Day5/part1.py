from Map import parse_input, seeds_to_locations

if __name__ == "__main__":
    seeds, map_blocks = parse_input("input.txt")
    locations = list(seeds_to_locations(seeds, map_blocks))
    print(min(locations))
