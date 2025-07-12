if __name__ == "__main__":
    total = 0
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            digits = [char for char in line if char.isdigit()]
            if digits:
                total += int(digits[0] + digits[-1])
    print(total)
