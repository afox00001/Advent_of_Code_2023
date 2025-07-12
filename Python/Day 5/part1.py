from Map import parse_input, apply_maps_to_value

if __name__ == "__main__":
    seeds, map_layers = parse_input("input.txt")
    locations = [apply_maps_to_value(seed, map_layers) for seed in seeds]
    print(min(locations))
