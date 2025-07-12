from collections import OrderedDict

def raw_directions_to_tuple(raw_directions):
    return (raw_directions.split(",")[0].replace("(", "").replace(" ", ""), raw_directions.split(",")[1].replace(")", "").replace(" ", ""))

if __name__ == "__main__":
    instructions = ""
    nodes = {}
    with open("input.txt") as file:
        for i, line in enumerate(file.readlines()):
            line = line.strip()
            if i == 0:
                instructions = line
                continue
            if line == "":
                continue
            nodes[line.split("=")[0].strip()] = raw_directions_to_tuple(line.split("=")[1])
    nodes = OrderedDict(sorted(nodes.items()))

    is_solved = False
    number_of_steps = 0
    current_node = "AAA"
    print(instructions)
    print(type(instructions))

    while not is_solved:
        for instruction in instructions:
            print("'" + instruction + "'")
            if current_node == "ZZZ":
                is_solved = True
                break
            print("'" + instruction + "'")
            if instruction == "L":
                current_node = nodes[current_node][0]
            elif instruction == "R":
                current_node = nodes[current_node][1]
            number_of_steps += 1

    print("Number of steps: {}".format(number_of_steps))
