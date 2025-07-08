if __name__ == "__main__":
    number_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    word_to_digit = {word: str(i + 1) for i, word in enumerate(number_words)}

    def find_all(a_str, sub):
        start = 0
        while True:
            start = a_str.find(sub, start)
            if start == -1:
                return
            yield start
            start += len(sub)

    total = 0
    with open("input.txt", "r") as inputFile:
        for line in inputFile.read().lower().split("\n"):
            digit_map = {}

            # Add word-based numbers
            for word, digit in word_to_digit.items():
                for i in find_all(line, word):
                    digit_map[i] = digit

            # Add character digits
            for i, char in enumerate(line):
                if char.isdigit():
                    digit_map[i] = char

            if not digit_map:
                continue  # Skip line if no digits found

            # Sort by position and extract first and last digits
            ordered_digits = [digit_map[i] for i in sorted(digit_map)]
            total += int(ordered_digits[0] + ordered_digits[-1])

    print(total)