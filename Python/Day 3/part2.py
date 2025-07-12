from text_parser import Graph, text_file_to_table, does_cell_meet_criteria

if __name__ == "__main__":
    table = text_file_to_table("input.txt")
    sum_of_gear_ratios = 0

    graph = Graph()
    graph.make_graph_from_table(table)

    gear_map = {}  # (x, y) of '*' > list of adjacent numbers
    current_number = ""
    meets_criteria = False
    current_char_pos = None

    for key, cell in graph.graph.items():
        if cell[0].isdigit():
            current_number += cell[0]
            char_meets_criteria = does_cell_meet_criteria(cell, graph, "*")
            if char_meets_criteria:
                meets_criteria = True
                current_char_pos = char_meets_criteria

        elif current_number:
            if meets_criteria:
                try:
                    gear_map[current_char_pos].append(int(current_number))
                except KeyError:
                    gear_map[current_char_pos] = [int(current_number)]
            current_number = ""
            meets_criteria = False

    # Handle case where last number is at the end of the file
    if current_number and meets_criteria:
        try:
            gear_map[current_char_pos].append(int(current_number))
        except KeyError:
            gear_map[current_char_pos] = [int(current_number)]

    # Calculate gear ratios
    for (x, y), nums in gear_map.items():
        if len(nums) == 2:
            sum_of_gear_ratios += nums[0] * nums[1]

    print(sum_of_gear_ratios)
