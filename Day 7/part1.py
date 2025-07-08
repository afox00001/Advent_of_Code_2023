from Hand import *

hands = []
with open("input.txt") as file:
    for line in file.readlines():
        cards = line.split(" ")[0]
        bet = int(line.split(" ")[1])
        hands.append(Hand(cards, bet))
hands.sort()

sum = 0
for i, hand in enumerate(hands):
    sum += hand.bet * (i + 1)
print(f"Sum: {sum}")
