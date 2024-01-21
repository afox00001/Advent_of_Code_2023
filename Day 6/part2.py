with open("input.txt", "r") as input_file:
    input_file_lines = input_file.readlines()

    lines = []
    for line in input_file_lines:
        lines.append(list(filter("".__ne__, line.split(":")[1].replace("\n", "").replace(" ", ""))))

    times_str = ""
    distances_str = ""

    times = []
    distances = []
    for time in lines[0]:
        times_str += time
    times = int(times_str)
    for distance in lines[1]:
        distances_str += distance
    greatest_distance = int(distances_str)

    number_of_ways_to_win = 0
    for speed in range(times + 1):
        distance = (times - speed) * speed
        if distance > greatest_distance:
            number_of_ways_to_win += 1
    print(number_of_ways_to_win)
