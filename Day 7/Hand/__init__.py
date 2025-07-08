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
        if self.is_five_of_a_kind():
            self.hand_type = HandType().five_of_a_kind
        elif self.is_four_of_a_kind():
            self.hand_type = HandType().four_of_a_kind
        elif self.is_full_house():
            self.hand_type = HandType().full_house
        elif self.is_three_of_a_kind():
            self.hand_type = HandType().three_of_a_kind
        elif self.is_two_pair():
            self.hand_type = HandType().two_pair
        elif self.is_pair():
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

    def is_five_of_a_kind(self):
        return self.has_n_of_a_kind(5)

    def is_four_of_a_kind(self):
        return self.has_n_of_a_kind(4)

    def is_three_of_a_kind(self):
        return self.has_n_of_a_kind(3)

    def is_two_pair(self):
        duplicates = self.number_of_duplicate_cards()
        number_of_pairs = 0
        for card in duplicates:
            if duplicates[card] == 2:
                number_of_pairs += 1
        return number_of_pairs == 2

    def is_pair(self):
        return self.has_n_of_a_kind(2)

    def is_full_house(self):
        return self.is_pair() and self.is_three_of_a_kind()

    def has_n_of_a_kind(self, n):
        duplicates = self.number_of_duplicate_cards()
        for card in duplicates:
            if duplicates[card] == n:
                return True
        return False

    def number_of_duplicate_cards(self):
        char_count_dict = {}
        for char in self.cards:
            if char in char_count_dict:
                char_count_dict[char] += 1
            else:
                char_count_dict[char] = 1
        return char_count_dict


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
