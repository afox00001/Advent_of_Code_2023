with open("input.txt", "r") as input_file:
    input_file_lines = input_file.readlines()

    lines = []
    for line in input_file_lines:
        lines.append(list(filter(("").__ne__, line.split(":")[1].replace("\n", "").split(" "))))
    times_str = lines[0]
    distances_str = lines[1]

    times = []
    distances = []
    for time in times_str:
        times.append(int(time))
    for distance in distances_str:
        distances.append(int(distance))

    greatest_distances = []
    list_of_ways_to_win = []
    i = 0
    for time in times:
        greatest_distance = distances[i]
        number_of_ways_to_win = 0
        i += 1
        for speed in range(time + 1):
            distance = (time - speed) * speed
            if distance > greatest_distance:
                number_of_ways_to_win += 1
        list_of_ways_to_win.append(number_of_ways_to_win)
        greatest_distances.append(greatest_distance)

    product = 1
    for i in list_of_ways_to_win:
        product *= i
    print(product)
