if __name__ == '__main__':
    with open("input.txt", "r") as file:
        lines = [line.split(":")[1].replace(" ", "").strip() for line in file]

    time = int(lines[0])
    distance_record = int(lines[1])

    ways_to_win = 0
    for speed in range(time + 1):
        travel_distance = speed * (time - speed)
        if travel_distance > distance_record:
            ways_to_win += 1

    print(ways_to_win)
