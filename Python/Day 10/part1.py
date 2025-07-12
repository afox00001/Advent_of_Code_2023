def get_index_of_char_in_str(string: str, search_char: str) -> int:
    return next((i for i, char in enumerate(string) if char == search_char), None)

with open("input.txt") as file:
    for line in file:
        line = line.strip()
        if "S" in line:
            line_arr = [char for char in line]
            print("'" + line + "'")
            S_char_index = get_index_of_char_in_str(line, "S")
            print(S_char_index)
            if S_char_index == len(line) - 1:
                print(line_arr[S_char_index - 1])
            elif S_char_index == len(line) + 1:
                print(line_arr[S_char_index + 1])
            else:
                print(line_arr[S_char_index - 1])
                print(line_arr[S_char_index + 1])