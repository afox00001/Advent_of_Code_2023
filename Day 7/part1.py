from Hand import *

if __name__ == "__main__":
    hands = []
    with open("input.txt") as file:
        for line in file:
            parts = line.strip().split()
            cards = list(parts[0].strip())
            bet = int(parts[1])
            hands.append(Hand(cards, bet))
    hands.sort()

    total = 0
    for i, hand in enumerate(hands):
        total += hand.bet * (i + 1)
    print(f"Sum: {total}")
