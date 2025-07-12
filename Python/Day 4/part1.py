if __name__ == "__main__":
    total_points = 0

    with open("input.txt", "r") as file:
        for ticket in file:
            ticket = ticket.strip()
            numbers_section = ticket.split(":")[1]
            winning_numbers = numbers_section.split("|")[0].split()
            card_numbers = numbers_section.split("|")[1].split()

            match_count = sum(1 for num in card_numbers if num in winning_numbers)

            if match_count > 0:
                total_points += 2 ** (match_count - 1)

    print(total_points)
