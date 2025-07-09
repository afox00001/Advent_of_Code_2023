def compute_next_value(seq):
    history = [seq]
    while any(x != 0 for x in history[-1]):
        prev = history[-1]
        diff = [b - a for a, b in zip(prev, prev[1:])]
        history.append(diff)

    # Extrapolate the next value from the bottom up
    next_val = 0
    for row in reversed(history):
        next_val = row[-1] + next_val
    return next_val


total_sum = 0
with open("input.txt") as file:
    for line in file:
        numbers = list(map(int, line.strip().split()))
        total_sum += compute_next_value(numbers)

print("Sum:", total_sum)