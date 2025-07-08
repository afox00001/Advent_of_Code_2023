from text_parser import Graph, does_cell_meet_criteria

if __name__ == "__main__":
    table = []
    part_number_codes_sum = 0
    with open("input.txt", "r") as inputFile:
        for line in inputFile.readlines():
            current_number = ""
            current_line = list(line.strip())
            table.append(current_line)

    numbers = []

    graph = Graph()
    graph.make_graph_from_table(table)

    current_number = ""
    meets_criteria = False
    for key, cell in graph.graph.items():
        if cell[0].isdigit():
            current_number += cell[0]
            if does_cell_meet_criteria(cell, graph):
                meets_criteria = True
        elif current_number:
            if meets_criteria:
                numbers.append(current_number)
            current_number = ""
            meets_criteria = False

    for number in numbers:
        part_number_codes_sum += int(number)

    print(part_number_codes_sum)
