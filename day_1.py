from loaders import load_list_from_lines

items = load_list_from_lines("data/day_1_1")

safe_value = 50
zeros_counter = 0
zero_passes_counter = 0

for item in items:
    direction = item[0]
    number = int(item[1:])

    if direction == "R":
        step = 1
    elif direction == "L":
        step = -1
    else:
        raise ValueError("direction must be 'R' or 'L'")

    for _ in range(number):
        # -10 % 100 = 90
        safe_value = (safe_value + step) % 100
        if safe_value == 0:
            zero_passes_counter += 1

    if safe_value % 100 == 0:
        zeros_counter += 1


print(f"Day 1_1 result is {zeros_counter}")
print(f"Day 1_2 result is {zero_passes_counter}")
