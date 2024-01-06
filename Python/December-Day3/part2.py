from text_parser import Graph, text_file_to_table, does_cell_meet_criteria

if __name__ == "__main__":
    table = text_file_to_table("input.txt")
    sum_of_gear_ratios = 0

    numbers = []

    graph = Graph()
    graph.make_graph_from_table(table)

    current_number = ""
    meets_criteria = False
    current_char_pos = None
    list_of_char_poses = {}
    for key, char in graph.graph.items():
        if char[0].isdigit():
            current_number += char[0]
            char_meets_criteria = does_cell_meet_criteria(char, graph, "*")
            if char_meets_criteria:
                meets_criteria = True
                current_char_pos = char_meets_criteria

        elif meets_criteria:
            numbers.append(current_number)
            try:
                list_of_char_poses[current_char_pos].append(int(current_number))
            except:
                list_of_char_poses[current_char_pos] = [int(current_number)]
            current_number = ""
            meets_criteria = False
        else:
            current_number = ""

    for x, y in list_of_char_poses:
        if len(list_of_char_poses[(x, y)]) == 2:
            sum_of_gear_ratios += list_of_char_poses[(x, y)][0] * list_of_char_poses[(x, y)][1]

    print(sum_of_gear_ratios)
