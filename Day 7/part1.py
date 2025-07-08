class HandType:
    def __init__(self):
        self.five_of_a_kind = 1
        self.four_of_a_kind = 2
        self.full_house = 3
        self.three_of_a_kind = 4
        self.two_pair = 5
        self.pair = 6
        self.high_card = 7


class Hand:
    def __init__(self, cards, bet):
        self.cards = cards
        self.bet = bet
        if is_five_of_a_kind(cards):
            self.hand_type = HandType().five_of_a_kind
        elif is_four_of_a_kind(cards):
            self.hand_type = HandType().four_of_a_kind
        elif is_full_house(cards):
            self.hand_type = HandType().full_house
        elif is_three_of_a_kind(cards):
            self.hand_type = HandType().three_of_a_kind
        elif is_two_pair(cards):
            self.hand_type = HandType().two_pair
        elif is_pair(cards):
            self.hand_type = HandType().pair
        else:
            self.hand_type = HandType().high_card


def sort_hands(hands):
    hands.sort(key=lambda e: e.hand_type)
    n = len(hands)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            hand1 = hands[j]
            hand2 = hands[j + 1]

            if hand1.hand_type < hand2.hand_type:
                swapped = True
                hands[j], hands[j + 1] = hands[j + 1], hands[j]
            else:
                tie_breaker = settle_tie(hand1.cards, hand2.cards)
                if hand1.cards == tie_breaker:
                    swapped = True
                    hands[j], hands[j + 1] = hands[j + 1], hands[j]
        if not swapped:
            return


def number_of_duplicates(str_obj):
    char_count_dict = {}
    for char in str_obj:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict


def is_five_of_a_kind(str_obj):
    duplicates = number_of_duplicates(str_obj)
    for card in duplicates:
        if duplicates[card] == 5:
            return True
    return False


def is_four_of_a_kind(str_obj):
    duplicates = number_of_duplicates(str_obj)
    for card in duplicates:
        if duplicates[card] == 4:
            return True
    return False


def is_three_of_a_kind(str_obj):
    duplicates = number_of_duplicates(str_obj)
    for card in duplicates:
        if duplicates[card] == 3:
            return True
    return False


def is_two_pair(str_obj):
    duplicates = number_of_duplicates(str_obj)
    for card in duplicates:
        if duplicates[card] == 2:
            return True
    return False


def is_pair(str_obj):
    duplicates = number_of_duplicates(str_obj)
    number_of_pairs = 0
    for card in duplicates:
        if duplicates[card] == 2:
            return True
    return False
    
    
def contains_pair(str_obj):
    duplicates = number_of_duplicates(str_obj)
    for card in duplicates:
        if duplicates[card] == 2:
            return True
    return False


def is_full_house(str_obj):
    return contains_pair(str_obj) and is_three_of_a_kind(str_obj)


def card_to_number(card):
    if card == "A":
        return 14
    elif card == "K":
        return 13
    elif card == "Q":
        return 12
    elif card == "J":
        return 11
    elif card == "T":
        return 10
    return int(card)


def settle_tie(hand1, hand2):
    for i, card1 in enumerate(hand1):
        card2 = card_to_number(hand2[i])
        card1 = card_to_number(card1)
        if card1 > card2:
            return hand1
        elif card1 < card2:
            return hand2

hands = []
with open("input.txt") as file:
    for line in file.readlines():
        cards = line.split(" ")[0]
        bet = int(line.split(" ")[1])
        hands.append(Hand(cards, bet)
sort_hands(hands)

sum = 0
for i, hand in enumerate(hands):
    sum += hand.bet * (i + 1)
print(f"Sum: {sum}")
