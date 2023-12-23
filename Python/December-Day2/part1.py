if __name__ == "__main__":

    game_ids_possible = 0

    number_of_red_cubes = 12
    number_of_green_cubes = 13
    number_of_blue_cubes = 14
    with open("input.txt", "r") as inputFile:
        for i in inputFile.readlines():
            game_id = int(i.split("Game")[1].split(":")[0].replace(" ", ""))
            chosen_cubes = i.split(":")[1].split(";")
            cube = ""
            is_game_possible = True
            for current_draw_selection in chosen_cubes:
                red_cube_for_this_selection = 0
                green_cube_for_this_selection = 0
                blue_cube_for_this_selection = 0

                current_draw_selection = current_draw_selection.replace("\n", "")
                if "," in current_draw_selection:
                    cube = current_draw_selection.split(",")
                else:
                    cube = current_draw_selection

                for cube_color in cube:
                    if "red" in cube_color:
                        red_cube_for_this_selection = int(cube_color.split("red")[0].replace(" ", ""))
                    elif "green" in cube_color:
                        green_cube_for_this_selection = int(cube_color.split("green")[0].replace(" ", ""))
                    elif "blue" in cube_color:
                        blue_cube_for_this_selection = int(cube_color.split("blue")[0].replace(" ", ""))
                    if red_cube_for_this_selection > number_of_red_cubes or green_cube_for_this_selection > number_of_green_cubes or blue_cube_for_this_selection > number_of_blue_cubes:
                        is_game_possible = False
                        break
            if not is_game_possible:
                continue
            else:
                game_ids_possible += game_id
    print(game_ids_possible)
