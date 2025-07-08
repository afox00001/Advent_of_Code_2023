if __name__ == "__main__":

    max_red = 12
    max_green = 13
    max_blue = 14

    total_possible_game_ids = 0

    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            # Parse Game ID
            game_id = int(line.split("Game")[1].split(":")[0].strip())

            # Get all draw sections
            draw_sections = line.split(":")[1].split(";")

            is_possible = True

            for draw in draw_sections:
                # Reset per draw
                red = green = blue = 0

                # Split into individual cube counts
                cube_parts = draw.strip().split(",")

                for part in cube_parts:
                    part = part.strip()
                    if "red" in part:
                        red += int(part.replace("red", "").strip())
                    elif "green" in part:
                        green += int(part.replace("green", "").strip())
                    elif "blue" in part:
                        blue += int(part.replace("blue", "").strip())

                # Check limits
                if red > max_red or green > max_green or blue > max_blue:
                    is_possible = False
                    break

            if is_possible:
                total_possible_game_ids += game_id

    print(total_possible_game_ids)
