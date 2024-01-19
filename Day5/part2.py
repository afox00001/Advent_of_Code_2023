from Map import line_to_list_of_map_ranges, map_src_list_to_dest_list, Map
def remove_overlap(ranges):
    result = []
    current_start = -1
    current_stop = -1

    for start, stop in sorted(ranges):
        if start > current_stop:
            # this segment starts after the last segment stops
            # just add a new segment
            result.append( (start, stop) )
            current_start, current_stop = start, stop
        else:
            # segments overlap, replace
            result[-1] = (current_start, stop)
            # current_start already guaranteed to be lower
            current_stop = max(current_stop, stop)

    return result
if __name__ == "__main__":
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

        i = 0
        list_of_seed_ranges = []
        temp_seed_range = []
        for seed in seeds:
            if i == 0:
                temp_seed_range.append(int(seed))
            if i == 1:
                temp_seed_range.append(int(seed) + temp_seed_range[0])
                list_of_seed_ranges.append(temp_seed_range)
                temp_seed_range = []
                i = 0
                continue
            i += 1
        print(list_of_seed_ranges)
        print(remove_overlap(list_of_seed_ranges))
        list_of_seed_ranges = remove_overlap(list_of_seed_ranges)
        # Making The Maps
        seed_soil = line_to_list_of_map_ranges(lines[2])
        soil_fertilizer = line_to_list_of_map_ranges(lines[3])
        fertilizer_water = line_to_list_of_map_ranges(lines[4])
        water_light = line_to_list_of_map_ranges(lines[5])
        light_temp = line_to_list_of_map_ranges(lines[6])
        temp_humidity = line_to_list_of_map_ranges(lines[7])
        humidity_location = line_to_list_of_map_ranges(lines[8])

        min_location = None
        for seed_range in list_of_seed_ranges:
            seeds = range(seed_range[0], seed_range[1])
            # Making The List of Mapped Destinations
            list_of_soils = map_src_list_to_dest_list(seeds, seed_soil)
            list_of_fertilizers = map_src_list_to_dest_list(list_of_soils, soil_fertilizer)
            list_of_waters = map_src_list_to_dest_list(list_of_fertilizers, fertilizer_water)
            list_of_lights = map_src_list_to_dest_list(list_of_waters, water_light)
            list_of_temps = map_src_list_to_dest_list(list_of_lights, light_temp)
            list_of_humidity = map_src_list_to_dest_list(list_of_temps, temp_humidity)
            list_of_locations = map_src_list_to_dest_list(list_of_humidity, humidity_location)

            if min_location is None:
                min_location = min(list_of_locations)
            elif min(list_of_locations) < min_location:
                min_location = min(list_of_locations)
            print(f"BATCH MIN LOCATION: {min_location}")

        print(min_location)
