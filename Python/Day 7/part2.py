from Hand import *

# --- Using the Hand class to compute total winnings ---
# Parse input lines into Hand objects
hands = []
with open("input.txt") as f:  # ensure the input file path is correct
    for line in f:
        if not line.strip():
            continue
        cards, bet = line.split()
        hands.append(Hand(cards, int(bet)))

# Sort hands by strength (using __lt__ defined in Hand)
hands.sort()

# Calculate total winnings: sum of bet * rank (1-based rank, weakest = 1)
total_winnings = 0
num_hands = len(hands)
for rank, hand in enumerate(hands, start=1):
    # The weakest hand gets rank 1, so the hand at index 0 (after sorting) is rank 1.
    # Therefore, we can multiply each bet by its (index+1) as rank.
    total_winnings += rank * hand.bet

print("Total winnings:", total_winnings)
