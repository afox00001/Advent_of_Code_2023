if __name__ == "__main__":
    with open("input.txt", "r") as input:
        input_text_lines = input.readlines()
        total_tickets_won = 0

        cards = {}  # Dict of card numbers, and how many cards that specific card won
        max_card_number = 0
        for ticket in input_text_lines:
            cards_points = 0

            card_number = int(ticket.replace("\n", "").split(":")[0].split("Card ")[1])

            if card_number > max_card_number:
                max_card_number = card_number

            winning_numbers = ticket.replace("\n", "").split(":")[1].split("|")[0].split(" ")
            winning_numbers = list(filter(("").__ne__, winning_numbers))

            card_numbers = ticket.replace("\n", "").split(":")[1].split("|")[1].split(" ")
            card_numbers = list(filter(("").__ne__, card_numbers))

            has_card_matched_a_wining_number = False
            for cards_card_number in card_numbers:
                if cards_card_number in winning_numbers:
                    has_card_matched_a_wining_number = True
                    cards_points += 1
                    try:
                        cards[card_number][1] += 1
                    except:
                        cards[card_number] = [1, 1]
            if not has_card_matched_a_wining_number:
                cards[card_number] = [1, 0]
        for card_number in cards:
            number_of_wining_numbers_on_card = cards[card_number][1]
            for i in range(card_number + 1, card_number + number_of_wining_numbers_on_card + 1):
                if i > max_card_number:
                    break
                try:
                    cards[i][0] += cards[card_number][0]

                except:
                    cards[i] = [1, 0]

        card_sum = 0
        for i in cards:
            card_sum += cards[i][0]
        print(card_sum)
