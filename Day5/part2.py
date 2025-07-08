from Map import seeds_to_locations
import numpy
from threading import Thread


def remove_overlap(ranges):
    result = []
    current_start = -1
    current_stop = -1

    for start, stop in sorted(ranges):
        if start > current_stop:
            # this segment starts after the last segment stops
            # just add a new segment
            result.append((start, stop))
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
        list_of_min_locations = []


        def process_seed_range(seed_range: iter):
            min_location = None
            seeds = numpy.arange(seed_range[0], seed_range[1], 1)
            # Making The List of Mapped Destinations
            for i in seeds_to_locations(seeds, lines):
                if i < min_location or i = None:
                    min_location = i
            seeds = []
            print(f"BATCH MIN LOCATION: {min_location}")
            list_of_min_locations.append(min_location)


        threads = [Thread(target=process_seed_range, args=[i]) for i in list_of_seed_ranges]
        [t.start() for t in threads]
        [t.join() for t in threads]
        print()
        print(f"RESULTS: {min(list_of_min_locations)}")
