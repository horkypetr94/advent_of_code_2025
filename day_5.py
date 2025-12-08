from loaders import load_list_from_lines

id_ranges = load_list_from_lines("data/day_5_1")
values = load_list_from_lines("data/day_5_2")

int_ranges = []
for id_range in id_ranges:
    start, end = id_range.split("-")
    int_ranges.append((int(start), int(end)))

fresh_items_counter = 0
for value in values:
    for start, end in int_ranges:
        if start <= int(value) and int(value) <= end:
            fresh_items_counter += 1
            break

print(f"result 1: {fresh_items_counter}")


int_ranges.sort(key=lambda i: i[0])

merged_ranges = []
for start, end in int_ranges:
    if not merged_ranges:
        merged_ranges.append((start, end))
        continue
    current_range = merged_ranges[-1]
    if current_range[0] <= start <= current_range[1]:
        merged_ranges[-1] = (current_range[0], max(current_range[1], end))
    else:
        merged_ranges.append((start, end))

counter = 0
for merged_range in merged_ranges:
    counter += (merged_range[1] - merged_range[0]) + 1
print(f"result 2: {counter}")
