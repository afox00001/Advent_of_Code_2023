class Graph:
    def __init__(self):
        self.graph = {}

    def make_graph_from_table(self, table: iter) -> None:
        for y, row in enumerate(table):
            for x, char in enumerate(row):
                neighbors = [
                    (x - 1, y) if x > 0 else None,
                    (x + 1, y) if x < len(row) - 1 else None,
                    (x, y - 1) if y > 0 else None,
                    (x, y + 1) if y < len(table) - 1 else None,
                    (x - 1, y - 1) if x > 0 and y > 0 else None,
                    (x + 1, y - 1) if x < len(row) - 1 and y > 0 else None,
                    (x - 1, y + 1) if x > 0 and y < len(table) - 1 else None,
                    (x + 1, y + 1) if x < len(row) - 1 and y < len(table) - 1 else None,
                    (x, y),
                ]
                self.graph[(x, y)] = [char] + neighbors

def text_file_to_table(file_location: str) -> list:
    table = []
    with open(file_location, "r") as inputFile:
        for line in inputFile:
            table.append([char for char in line.strip() if char != " "])
    return table


def does_cell_meet_criteria(cell: iter, graph: iter, special_chars_in_criteria="!@#$%^&*()_-=+/\\") -> iter or bool:
    if cell[0].isdigit():
        for i in range(1, 9):
            if cell[i] is not None:
                if graph.graph[cell[i]][0] in special_chars_in_criteria:
                    return cell[i]
    return False
