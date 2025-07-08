with open("input.txt", "r") as input_file:
    lines = [line.split(":")[1].strip().split() for line in input_file]

times = list(map(int, lines[0]))
distances = list(map(int, lines[1]))

product = 1

for time, record_distance in zip(times, distances):
    ways_to_win = 0
    for speed in range(time + 1):
        distance = speed * (time - speed)
        if distance > record_distance:
            ways_to_win += 1
    product *= ways_to_win

print(product)
