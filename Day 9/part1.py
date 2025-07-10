from calculate_values import *

with open("input.txt") as file:
    total_sum = get_total_sum_for_all_extrapolations(file.readlines(), is_calculating_right_side_of_pyramid=True)
print("Sum:", total_sum)
