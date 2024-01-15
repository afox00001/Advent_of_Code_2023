class Map:
    def __init__(self):
        self.dest_start = None
        self.src_start = None
        self.range = None

        self.dest_list = []
        self.src_list = []


def line_to_list_of_map_ranges(line):
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


def get_destination_from_map_and_obj(map, obj):
    if (map.src_start + map.range) >= obj and map.src_start <= obj:
        return (map.dest_start - map.src_start) + obj


def map_src_list_to_dest_list(src_list, maps):
    dest_list = []
    for src_item in src_list:
        for map in maps:
            dest = None
            dest_check = get_destination_from_map_and_obj(map, src_item)
            if dest_check is not None:
                dest = dest_check
                break
        if dest is not None:
            dest_list.append(dest)
        else:
            dest_list.append(src_item)
    return dest_list


with open("input.txt", "r") as input_file:
    input_text = input_file.read()
    lines = []
    for i in input_text.split(":"):
        new_line = ""
        for y in i:
            if y.isdigit():
                new_line += y
            elif y == " " or y == "\n":
                new_line += " "
        lines.append(new_line)

    seeds = lines[1].split(" ")
    seeds = list(filter(("").__ne__, seeds))
    seeds = [int(i) for i in seeds]

    #Making The Maps
    seed_soil = line_to_list_of_map_ranges(lines[2])
    soil_fertilizer = line_to_list_of_map_ranges(lines[3])
    fertilizer_water = line_to_list_of_map_ranges(lines[4])
    water_light = line_to_list_of_map_ranges(lines[5])
    light_temp = line_to_list_of_map_ranges(lines[6])
    temp_humidity = line_to_list_of_map_ranges(lines[7])
    humidity_location = line_to_list_of_map_ranges(lines[8])

    #Making The List of Mapped Destinations
    list_of_soils = map_src_list_to_dest_list(seeds, seed_soil)
    list_of_fertilizers = map_src_list_to_dest_list(list_of_soils, soil_fertilizer)
    list_of_waters = map_src_list_to_dest_list(list_of_fertilizers, fertilizer_water)
    list_of_lights = map_src_list_to_dest_list(list_of_waters, water_light)
    list_of_temps = map_src_list_to_dest_list(list_of_lights, light_temp)
    list_of_humidity = map_src_list_to_dest_list(list_of_temps, temp_humidity)
    list_of_locations = map_src_list_to_dest_list(list_of_humidity, humidity_location)

    print(min(list_of_locations))
