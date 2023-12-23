with open("input.txt", "r") as inputFile:
    sum = 0
    for line in inputFile.read().split("\n"):
        number = ""
        for char in line:
            if char.isdigit():
                number += char
        sum += int(number[0] + number[-1])
    print(sum)