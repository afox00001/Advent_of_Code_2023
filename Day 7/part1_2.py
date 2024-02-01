cards = {}
with open("input.txt") as file:
    for line in file.readlines():
        cards[line.split(" ")[0]] = line.split(" ")[1]


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
    number_of_pairs = 0
    for card in duplicates:
        if duplicates[card] == 2:
            number_of_pairs += 1
        elif duplicates[card] > 2:
            return False
    return True if number_of_pairs == 2 else False

def is_pair(str_obj):
    duplicates = number_of_duplicates(str_obj)
    number_of_pairs = 0
    for card in duplicates:
        if duplicates[card] == 2:
            number_of_pairs += 1
        elif duplicates[card] > 2:
            return False

    return True if number_of_pairs == 1 else False

for hand in cards:
    if is_pair(hand):
        print(hand)