class Graph:
    def __init__(self):
        self.graph = {}

    def make_graph_from_table(self, table: iter) -> None:

        for y, row in enumerate(table):
            for x, char in enumerate(row):
                left = x - 1, y if x > 0 else None
                right = x + 1, y if x < len(row) - 1 else None
                top = x, y - 1 if y > 0 else None
                bottom = x, y + 1 if y < len(table) - 1 else None
                top_left = x - 1, y - 1 if x > 0 and y > 0 else None
                top_right = x + 1, y - 1 if y > 0 and x < len(row) - 1 else None
                bottom_left = x - 1, y + 1 if y < len(table) - 1 and x > 0 else None
                bottom_right = x + 1, y + 1 if y < len(table) - 1 and x < len(row) - 1 else None

                self.graph[x, y] = [char, left, right, top, bottom, top_left, top_right, bottom_left,
                                    bottom_right, (x, y)]


def does_cell_meet_criteria(cell: iter, graph: iter) -> bool:
    special_chars_in_criteria = "!@#$%^&*()_-=+/\\"
    if cell[0].isdigit():
        for i in range(1, 9):
            if cell[i][0] is not None and cell[i][1] is not None:
                if graph.graph[(char[i][0], char[i][1])][0] in special_chars_in_criteria:
                    return True
    return False


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
