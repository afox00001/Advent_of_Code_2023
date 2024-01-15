from Map import line_to_list_of_map_ranges, map_src_list_to_dest_list, Map

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
        seeds = [int(i) for i in seeds]

        # Making The Maps
        seed_soil = line_to_list_of_map_ranges(lines[2])
        soil_fertilizer = line_to_list_of_map_ranges(lines[3])
        fertilizer_water = line_to_list_of_map_ranges(lines[4])
        water_light = line_to_list_of_map_ranges(lines[5])
        light_temp = line_to_list_of_map_ranges(lines[6])
        temp_humidity = line_to_list_of_map_ranges(lines[7])
        humidity_location = line_to_list_of_map_ranges(lines[8])

        # Making The List of Mapped Destinations
        list_of_soils = map_src_list_to_dest_list(seeds, seed_soil)
        list_of_fertilizers = map_src_list_to_dest_list(list_of_soils, soil_fertilizer)
        list_of_waters = map_src_list_to_dest_list(list_of_fertilizers, fertilizer_water)
        list_of_lights = map_src_list_to_dest_list(list_of_waters, water_light)
        list_of_temps = map_src_list_to_dest_list(list_of_lights, light_temp)
        list_of_humidity = map_src_list_to_dest_list(list_of_temps, temp_humidity)
        list_of_locations = map_src_list_to_dest_list(list_of_humidity, humidity_location)

        print(min(list_of_locations))
