if __name__ == "__main__":

    def max_color_in_game(game_text: str, color: str) -> int:
        max_found = 0
        # Split all draws
        draws = game_text.split(":")[1].split(";")
        for draw in draws:
            parts = draw.strip().split(",")
            for part in parts:
                if color in part:
                    try:
                        value = int(part.strip().split(" ")[0])
                        max_found = max(max_found, value)
                    except (ValueError, IndexError):
                        pass  # Skip malformed entries
        return max_found


    total_power = 0

    with open("input.txt", "r") as inputFile:
        for game in inputFile:
            red = max_color_in_game(game, "red")
            green = max_color_in_game(game, "green")
            blue = max_color_in_game(game, "blue")

            total_power += red * green * blue

    print(total_power)
