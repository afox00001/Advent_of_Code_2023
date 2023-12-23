def search_for_minimum_color(color: str, game_to_search) -> int:
    if color in game_to_search:
        color_cubes = []
        color_cubes_text_array = game_to_search.split(":")[1].split(color)
        color_cubes_text_array.pop()
        for i in color_cubes_text_array:
            color_cubes.append(int(i.split(" ")[-2]))
        return max(color_cubes)


sum_of_minimum_set_of_cubes = 0

with open("input.txt", "r") as inputFile:
    for game in inputFile.readlines():
        game_id = int(game.split("Game")[1].split(":")[0].replace(" ", ""))

        minimum_red_cubes = search_for_minimum_color("red", game)
        minimum_green_cubes = search_for_minimum_color("green", game)
        minimum_blue_cubes = search_for_minimum_color("blue", game)

        sum_of_minimum_set_of_cubes += (minimum_red_cubes * minimum_green_cubes * minimum_blue_cubes)

    print(sum_of_minimum_set_of_cubes)
