def extrapolate_next_value(sequence):
    # Build the difference pyramid
    difference_rows = [sequence]
    while any(value != 0 for value in difference_rows[-1]):
        previous_row = difference_rows[-1]
        next_row = [next_val - current_val for current_val, next_val in zip(previous_row, previous_row[1:])]
        difference_rows.append(next_row)

    # Predict the next value by adding back up the pyramid
    predicted_value = 0
    for row in reversed(difference_rows):
        predicted_value = row[0] + predicted_value
    return predicted_value


total_extrapolated_sum = 0
with open("input.txt") as file:
    for line in file:
        number_sequence = list(map(int, line.strip().split()))
        total_extrapolated_sum += extrapolate_next_value(number_sequence)

print("Sum:", total_extrapolated_sum)
