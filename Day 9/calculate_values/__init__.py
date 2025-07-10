def build_difference_pyramid(sequence: iter) -> iter:
    difference_rows = [sequence]
    while any(value != 0 for value in difference_rows[-1]):
        previous_row = difference_rows[-1]
        next_row = [next_val - current_val for current_val, next_val in zip(previous_row, previous_row[1:])]
        difference_rows.append(next_row)
    return difference_rows


def extrapolate_next_value(sequence: iter, is_calculating_right_side_of_pyramid: bool) -> iter:
    # Predict the next value by adding back up the pyramid
    predicted_value = 0
    for row in reversed(build_difference_pyramid(sequence)):
        if is_calculating_right_side_of_pyramid:
            predicted_value = row[0] + predicted_value
        else:
            predicted_value = row[0] - predicted_value
    return predicted_value

def get_total_sum_for_all_extrapolations(raw_text_lines_as_array: iter, is_calculating_right_side_of_pyramid: bool) -> iter:
    total_extrapolated_sum = 0
    for line in raw_text_lines_as_array:
        number_sequence = list(map(int, line.strip().split()))
        total_extrapolated_sum += extrapolate_next_value(number_sequence, is_calculating_right_side_of_pyramid)
    return total_extrapolated_sum