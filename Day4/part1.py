if __name__ == "__main__":
    with open("input.txt", "r") as input:
        input_text_lines = input.readlines()
        total_points = 0
        for ticket in input_text_lines:
            cards_points = 0
            winning_numbers = ticket.replace("\n", "").split(":")[1].split("|")[0].split(" ")
            winning_numbers = list(filter(("").__ne__, winning_numbers))

            card_numbers = ticket.replace("\n", "").split(":")[1].split("|")[1].split(" ")
            card_numbers = list(filter(("").__ne__, card_numbers))

            for card_number in card_numbers:
                if card_number in winning_numbers:
                    if cards_points == 0:
                        cards_points = 1
                    else:
                        cards_points *= 2
            total_points += cards_points
        print(total_points)