class Map:
    def __init__(self):
        self.dest_start = None
        self.src_start = None
        self.range = None

        self.dest_list = []
        self.src_list = []

    def enumerate_lists_from_ranges(self):
        pass


for i in range(0, 10):
    print(i)


def line_to_list_of_map_ranges(line):
    # print(line)
    line = line.split(" ")
    list_of_maps = []
    i = 0
    map = Map()
    # print(line)
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
        # print(new_line)
        # print()
    # print(lines)
    seeds = line_to_list_of_map_ranges(lines[1])
    seed_soil = line_to_list_of_map_ranges(lines[2])
    soil_fertilizer = line_to_list_of_map_ranges(lines[3])
    fertilizer_water = line_to_list_of_map_ranges(lines[4])
    water_light = line_to_list_of_map_ranges(lines[5])
    light_temp = line_to_list_of_map_ranges(lines[6])
    temp_humidity = line_to_list_of_map_ranges(lines[7])
    humidity_location = line_to_list_of_map_ranges(lines[8])

    print(seeds[0].dest_start)
