from loaders import load_list_of_lists
from tools import remap_lol_values, pad_lol_with_zeros, get_moore_neighbourhood

array = load_list_of_lists("data/day_4_1")
array = remap_lol_values(array, {".": 0, "@": 1})
array = pad_lol_with_zeros(array)


global_counter = 0
for i in range(1, len(array) - 1):
    for j in range(1, len(array[i]) - 1):
        surroundings = get_moore_neighbourhood(array, i, j)
        if array[i][j] == 1 and sum(surroundings) < 4:
            global_counter += 1

print(f"result 1: {global_counter}")


global_counter = 0
keep_iterating = True

while keep_iterating:
    new_array = array.copy()
    local_counter = 0
    for i in range(1, len(array) - 1):
        for j in range(1, len(array[i]) - 1):
            surroundings = get_moore_neighbourhood(array, i, j)
            if array[i][j] == 1 and sum(surroundings) < 4:
                local_counter += 1
                new_array[i][j] = 0

    global_counter += local_counter
    array = new_array.copy()
    if local_counter == 0:
        keep_iterating = False

print(f"result 2: {global_counter}")
