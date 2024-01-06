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


def text_file_to_table(file_location: str) -> iter:
    table = []
    with open("input.txt", "r") as inputFile:
        for line in inputFile.readlines():
            current_line = []
            current_number = ""
            for char in line:
                if char == " " or char == "\n":
                    continue
                current_line.append(char)
            table.append(current_line)
    return table

def does_cell_meet_criteria(cell: iter, graph: iter, special_chars_in_criteria="!@#$%^&*()_-=+/\\") -> iter or bool:
    if cell[0].isdigit():
        for i in range(1, 9):
            if cell[i][0] is not None and cell[i][1] is not None:
                if graph.graph[(cell[i][0], cell[i][1])][0] in special_chars_in_criteria:
                    return (cell[i][0], cell[i][1])
    return False