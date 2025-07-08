if __name__ == "__main__":
    from collections import defaultdict

    with open("input.txt", "r") as file:
        lines = [line.strip() for line in file]

    num_cards = len(lines)
    card_data = {}  # card_number -> number of matches
    copies = defaultdict(int)  # card_number -> number of total copies (including original)

    # Step 1: Parse all cards
    for line in lines:
        parts = line.split(":")
        card_number = int(parts[0].split("Card")[1].strip())
        win_section, my_section = parts[1].split("|")

        winning_numbers = set(win_section.strip().split())
        my_numbers = my_section.strip().split()

        match_count = sum(1 for n in my_numbers if n in winning_numbers)
        card_data[card_number] = match_count
        copies[card_number] = 1  # Start with one original copy

    # Step 2: Propagate wins
    for card_number in range(1, num_cards + 1):
        match_count = card_data.get(card_number, 0)
        for i in range(1, match_count + 1):
            copies[card_number + i] += copies[card_number]

    total = sum(copies.values())
    print(total)
