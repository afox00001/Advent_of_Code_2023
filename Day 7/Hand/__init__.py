from enum import IntEnum
from collections import Counter


class HandType(IntEnum):
    FIVE_OF_A_KIND = 1
    FOUR_OF_A_KIND = 2
    FULL_HOUSE = 3
    THREE_OF_A_KIND = 4
    TWO_PAIR = 5
    PAIR = 6
    HIGH_CARD = 7


class Hand:
    def __init__(self, cards, bet):
        self.cards = cards
        self.bet = bet
        if self.has_n_of_a_kind(5):
            self.hand_type = HandType.FIVE_OF_A_KIND
        elif self.has_n_of_a_kind(4):
            self.hand_type = HandType.FOUR_OF_A_KIND
        elif self.is_full_house():
            self.hand_type = HandType.FULL_HOUSE
        elif self.has_n_of_a_kind(3):
            self.hand_type = HandType.THREE_OF_A_KIND
        elif self.is_two_pair():
            self.hand_type = HandType.TWO_PAIR
        elif self.has_n_of_a_kind(2):
            self.hand_type = HandType.PAIR
        else:
            self.hand_type = HandType.HIGH_CARD

    def __lt__(self, other):
        if self.hand_type != other.hand_type:
            return self.hand_type > other.hand_type  # Higher hand_type = stronger = comes first
        else:
            winner = self.settle_tie(other)
            return winner == other  # If other wins the tie, self < other

    def __eq__(self, other):
        return self.hand_type == other.hand_type and self.cards == other.cards

    def is_two_pair(self):
        return list(self.get_card_counts().values()).count(2) == 2 # If there are 2 pairs in the hand

    def is_full_house(self):
        return self.has_n_of_a_kind(2) and self.has_n_of_a_kind(3)  # If has a pair, AND a 3 of a kind

    def has_n_of_a_kind(self, n):
        return n in self.get_card_counts().values()

    def get_card_counts(self):
        return Counter(self.cards)

    def settle_tie(self, hand2):
        for i, card1 in enumerate(self.cards):
            card2 = card_to_number(hand2.cards[i])
            card1 = card_to_number(card1)
            if card1 > card2:
                return self
            elif card1 < card2:
                return hand2
        return self # Default to "this" hand (self) if self and hand2 are truly the same

def card_to_number(card):
    face_cards = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    if isinstance(card, int): # If it's just a number card then it can just return the value
        return card
    if isinstance(card, str): # Otherwise, it will find out what value this face card (and 10) should be...
        card = card.upper().strip()
        if card in face_cards:
            return face_cards[card]
        elif card.isdigit():
            num = int(card)
            if 2 <= num <= 9:
                return num
    raise ValueError(f"Invalid card value: {card}") # If it fails at that, raise an error