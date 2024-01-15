class Map:
    def __init__(self):
        self.dest_start = None
        self.src_start = None


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
