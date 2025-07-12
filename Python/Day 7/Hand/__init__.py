from enum import IntEnum
from collections import Counter
from itertools import combinations_with_replacement, permutations


class HandType(IntEnum):
    FIVE_OF_A_KIND = 1
    FOUR_OF_A_KIND = 2
    FULL_HOUSE = 3
    THREE_OF_A_KIND = 4
    TWO_PAIR = 5
    PAIR = 6
    HIGH_CARD = 7


class Hand:
    def __init__(self, cards, bet, is_jacks_wild=False):
        self.original_cards = cards
        self.bet = bet
        self.is_jacks_wild = is_jacks_wild
        self.cards, self.hand_type = self.resolve_best_hand()

    def resolve_best_hand(self):
        if not self.is_jacks_wild or 'J' not in self.original_cards:
            counts = Counter(self.original_cards)
            return self.original_cards, get_hand_type_from_counts(counts)

        joker_count = self.original_cards.count('J')
        non_joker_cards = [c for c in self.original_cards if c != 'J']
        best_score = (float('inf'), [])  # (hand_type.value, numeric_hand)
        best_hand = self.original_cards

        for combo in combinations_with_replacement('23456789TQKA', joker_count):
            for perm in set(permutations(combo)):
                test_hand = non_joker_cards + list(perm)
                counts = Counter(test_hand)
                hand_type = get_hand_type_from_counts(counts)
                numeric_hand = [card_to_number(c, True) for c in test_hand]
                score = (hand_type.value, numeric_hand)
                if score < best_score:
                    best_score = score
                    best_hand = test_hand

        return best_hand, HandType(best_score[0])

    def __eq__(self, other):
        return self.hand_type == other.hand_type and self.cards == other.cards

    def __lt__(self, other):
        if self.hand_type != other.hand_type:
            return self.hand_type > other.hand_type  # lower is better
        return self.get_numeric_hand() < other.get_numeric_hand()

    def get_numeric_hand(self):
        return [card_to_number(c, self.is_jacks_wild) for c in self.cards]

    def __repr__(self):
        return f"Hand({self.cards}, {self.bet}, {self.hand_type.name})"


def get_hand_type_from_counts(counts):
    values = sorted(counts.values(), reverse=True)
    if values == [5]:
        return HandType.FIVE_OF_A_KIND
    elif values == [4, 1]:
        return HandType.FOUR_OF_A_KIND
    elif values == [3, 2]:
        return HandType.FULL_HOUSE
    elif values == [3, 1, 1]:
        return HandType.THREE_OF_A_KIND
    elif values == [2, 2, 1]:
        return HandType.TWO_PAIR
    elif values == [2, 1, 1, 1]:
        return HandType.PAIR
    else:
        return HandType.HIGH_CARD


def card_to_number(card, is_jacks_wild):
    if is_jacks_wild:
        face_cards = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, 'J': 1}
    else:
        face_cards = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    card = card.upper().strip()
    if card in face_cards:
        return face_cards[card]
    elif card.isdigit():
        return int(card)
    raise ValueError(f"Invalid card value: {card}")
