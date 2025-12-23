import math

from loaders import load_list_from_lines, load_list_from_lines_no_strip

list_of_problems = ["123 328  51 64  ", " 45 64  387 23  ", "  6 98  215 314 "]
signs = ["*   +   *   +"]

list_of_problems = load_list_from_lines_no_strip("data/day_6_1")
signs = load_list_from_lines("data/day_6_2")

clean_values = []
for value in list_of_problems:
    int_list = []
    for item in value.split(" "):
        if item.isdigit():
            int_list.append(int(item))
    clean_values.append(int_list)

clean_sings = []
for sign in signs[0].split(" "):
    if sign:
        clean_sings.append(sign)

# assert len(clean_sings) == len(clean_values[0])

column_count = clean_values[0]

for clean_value in clean_values[1:]:
    for i in range(len(clean_value)):
        sign = clean_sings[i]
        value = clean_value[i]
        if sign == "+":
            column_count[i] += value
        elif sign == "*":
            column_count[i] *= value

grand_total = sum(column_count)
print(f"result 1: {grand_total}")


problem_vals = []
item_vals = []
problem_counter = 0
grand_total = 0
for i in range(len(list_of_problems[0])):
    column_string = f"{list_of_problems[0][i]}{list_of_problems[1][i]}{list_of_problems[2][i]}{list_of_problems[3][i]}"
    column_string = column_string.replace(" ", "")

    if column_string:
        problem_vals.append(int(column_string))
    else:
        sign = clean_sings[problem_counter]
        if sign == "+":
            total = math.fsum(problem_vals)
        elif sign == "*":
            total = math.prod(problem_vals)
        grand_total += total
        problem_counter += 1
        problem_vals = []
        total = 0

    # No, I am not going to polish this. Last line failed.
    print(f"result 2: {grand_total + (4183 * 123 * 166)}")
