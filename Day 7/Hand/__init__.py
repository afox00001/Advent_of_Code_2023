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
        if self.has_n_of_a_kind(5):
            self.hand_type = HandType().five_of_a_kind
        elif self.has_n_of_a_kind(4):
            self.hand_type = HandType().four_of_a_kind
        elif self.is_full_house():
            self.hand_type = HandType().full_house
        elif self.has_n_of_a_kind(3):
            self.hand_type = HandType().three_of_a_kind
        elif self.is_two_pair():
            self.hand_type = HandType().two_pair
        elif self.has_n_of_a_kind(2):
            self.hand_type = HandType().pair
        else:
            self.hand_type = HandType().high_card

    def __lt__(self, other):
        if self.hand_type != other.hand_type:
            return self.hand_type > other.hand_type  # Higher hand_type = stronger = comes first
        else:
            winner = settle_tie(self.cards, other.cards)
            return winner == other.cards  # If other wins the tie, self < other

    def __eq__(self, other):
        return self.hand_type == other.hand_type and self.cards == other.cards

    def is_two_pair(self):
        duplicates = self.number_of_duplicate_cards()
        number_of_pairs = 0
        for card in duplicates:
            if duplicates[card] == 2:
                number_of_pairs += 1
        return number_of_pairs == 2

    def is_full_house(self):
        return self.has_n_of_a_kind(2) and self.has_n_of_a_kind(3)  # If has a pair, AND a 3 of a kind

    def has_n_of_a_kind(self, n):
        duplicates = self.number_of_duplicate_cards()
        for card in duplicates:
            if duplicates[card] == n:
                return True
        return False

    def number_of_duplicate_cards(self):
        card_occurrences = {}
        for card in self.cards:
            if card in card_occurrences:
                card_occurrences[card] += 1
            else:
                card_occurrences[card] = 1
        return card_occurrences


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
