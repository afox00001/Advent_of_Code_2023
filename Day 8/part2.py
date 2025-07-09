import math

def parse_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    instructions = lines[0]
    nodes = {}
    for line in lines[2:]:
        name, rest = line.split(" = ")
        left, right = rest.strip("()").split(", ")
        nodes[name] = (left, right)
    return instructions, nodes

def steps_to_z(start_node, instructions, nodes):
    steps = 0
    i = 0
    current = start_node
    while True:
        if current.endswith("Z"):
            return steps
        direction = instructions[i % len(instructions)]
        current = nodes[current][0] if direction == "L" else nodes[current][1]
        steps += 1
        i += 1

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def main(instructions, nodes):
    start_nodes = [name for name in nodes if name.endswith("A")]
    cycle_lengths = [steps_to_z(name, instructions, nodes) for name in start_nodes]
    result = cycle_lengths[0]
    for c in cycle_lengths[1:]:
        result = lcm(result, c)
    return result

if __name__ == "__main__":
    instructions, nodes = parse_input("input.txt")
    print("Part 2: All ghost nodes reach Z on step =", main(instructions, nodes))
