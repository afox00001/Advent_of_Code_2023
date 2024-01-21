class Map:
    def __init__(self):
        self.dest_start = None
        self.src_start = None
        self.range = None


def line_to_list_of_map_ranges(line: str) -> iter:
    line = line.split(" ")
    list_of_maps = []
    i = 0
    map = Map()
    for arg in line:
        if arg == "" or arg == "\n" or arg == " ":
            continue
        if i == 0:
            map.dest_start = int(arg)
        elif i == 1:
            map.src_start = int(arg)
        elif i == 2:
            map.range = int(arg)
            list_of_maps.append(map)
            map = Map()
            i = 0
            continue
        i += 1
    return list_of_maps


def map_src_list_to_dest_list(src_list: iter, maps: iter) -> iter:
    def get_destination_from_map_and_obj(map: Map, obj: int) -> int:
        if (map.src_start + map.range) >= obj and map.src_start <= obj:
            return (map.dest_start - map.src_start) + obj

    for src_item in src_list:
        for map in maps:
            dest = None
            dest_check = get_destination_from_map_and_obj(map, src_item)
            if dest_check is not None:
                dest = dest_check
                break
        if dest is not None:
            yield dest
        else:
            yield


def maps_and_src_to_dest(src, maps):
    def get_destination_from_map_and_obj(map: Map, obj: int) -> int:
        if (map.src_start + map.range) >= obj >= map.src_start:
            return (map.dest_start - map.src_start) + obj

    dest = None
    map_used = None
    for map in maps:
        dest_check = get_destination_from_map_and_obj(map, src)
        if dest_check is not None:
            dest = dest_check
            map_used = map
            break
    if dest is None:
        dest = src
    return dest


def is_in_range(value: int, range: tuple) -> bool:
    print(f"range: {range} value: {value}")
    return range[1] >= value >= range[0]


def maps_and_src_range_to_list_of_dest_ranges(src_range: iter, maps: iter) -> iter:
    dest_range_start_and_map = maps_and_src_to_dest(src_range[0], maps)
    dest_range_end_and_map = maps_and_src_to_dest(src_range[1], maps)

    list_of_dest_ranges = []

    if dest_range_start_and_map[1] != dest_range_end_and_map[
        1]:  # if the map used to find the dest_start != the map used to find the dest_end
        list_of_dest_ranges.append((dest_range_start_and_map[0], dest_range_end_and_map[1].src_start))
        list_of_dest_ranges.append((dest_range_end_and_map[1].src_start, src_range[1]))
        return list_of_dest_ranges
    return [(dest_range_start_and_map[0], dest_range_end_and_map[0])]

def seeds_to_locations(seeds: iter, lines: iter) -> iter:
    seed_soil = line_to_list_of_map_ranges(lines[2])
    soil_fertilizer = line_to_list_of_map_ranges(lines[3])
    fertilizer_water = line_to_list_of_map_ranges(lines[4])
    water_light = line_to_list_of_map_ranges(lines[5])
    light_temp = line_to_list_of_map_ranges(lines[6])
    temp_humidity = line_to_list_of_map_ranges(lines[7])
    humidity_location = line_to_list_of_map_ranges(lines[8])

    for seed in seeds:
        soil = maps_and_src_to_dest(seed, seed_soil)
        fertilizer = maps_and_src_to_dest(soil, soil_fertilizer)

        soil = []

        water = maps_and_src_to_dest(fertilizer, fertilizer_water)

        fertilizer = []

        light = maps_and_src_to_dest(water, water_light)

        water = []

        temp = maps_and_src_to_dest(light, light_temp)

        light = []

        humidity = maps_and_src_to_dest(temp, temp_humidity)

        temp = []

        yield maps_and_src_to_dest(humidity, humidity_location)

        humidity = []


