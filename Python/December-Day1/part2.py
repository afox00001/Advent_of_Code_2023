list_of_numbers_as_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
words_to_numbers_lookup_dict = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

with open("input.txt", "r") as inputFile:
    addedSum = 0
    for line in inputFile.read().lower().split("\n"):
        number = {}
        for digit in list_of_numbers_as_words:
            if digit in line:
                index = find_all(line, digit)
                for i in index:
                    #print(digit)
                    number[i] = str(words_to_numbers_lookup_dict[digit])
        for i, character in enumerate(line):
            if character.isdigit():
                number[i] = character
        #Sort the number dict by keys
        number_keys = list(number.keys())
        number_keys.sort()
        number = {i: number[i] for i in number_keys}

        number_as_str = ""
        for i in number:
            number_as_str += number[i]
        addedSum += int(number_as_str[0] + number_as_str[-1])

    print(addedSum)
