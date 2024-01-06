from text_parser import Graph, does_cell_meet_criteria

if __name__ == "__main__":
    table = []
    part_number_codes_sum = 0
    with open("input.txt", "r") as inputFile:
        for line in inputFile.readlines():
            current_line = []
            current_number = ""
            for char in line:
                if char == " " or char == "\n":
                    continue
                current_line.append(char)
            table.append(current_line)

    numbers = []

    graph = Graph()
    graph.make_graph_from_table(table)

    current_number = ""
    meets_criteria = False
    for key, char in graph.graph.items():
        if char[0].isdigit():
            current_number += char[0]
            if does_cell_meet_criteria(char, graph):
                meets_criteria = True
        elif meets_criteria:
            numbers.append(current_number)
            current_number = ""
            meets_criteria = False
        else:
            current_number = ""

    for number in numbers:
        part_number_codes_sum += int(number)

    print(part_number_codes_sum)
