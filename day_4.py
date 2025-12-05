from helpers import load_list_of_lists, remap_lol_values, pad_lol_with_zeros

array = load_list_of_lists("data/day_4_1")

array = [
    ['.', '.', '@', '@', '.', '@', '@', '@', '@', '.'],
    ['@', '@', '@', '.', '@', '.', '@', '.', '@', '@'],
    ['@', '@', '@', '@', '@', '.', '@', '.', '@', '@'],
    ['@', '.', '@', '@', '@', '@', '.', '.', '@', '.'],
    ['@', '@', '.', '@', '@', '@', '@', '.', '@', '@'],
    ['.', '@', '@', '@', '@', '@', '@', '@', '.', '@'],
    ['.', '@', '.', '@', '.', '@', '.', '@', '@', '@'],
    ['@', '.', '@', '@', '@', '.', '@', '@', '@', '@'],
    ['.', '@', '@', '@', '@', '@', '@', '@', '@', '.'],
    ['@', '.', '@', '.', '@', '@', '@', '.', '@', '.']
]
array = remap_lol_values(array, {".":0, "@": 1})
array = pad_lol_with_zeros(array)

moore_neighbouhood_dict = {
    "NW": (-1,-1),
    "N": (-1,0),
    "NE": (-1, 1),
    "W": (0,-1),
    "E": (0,1),
    "SW": (1,-1),
    "S": (1,0),
    "SE": (1,1),
}

def get_moore_neighbourhood(line, item):
    items = []
    for diff in moore_neighbouhood_dict.values():
        items.append(array[line+diff[0]][item+diff[1]])
    return items

global_counter = 0
for i in range(1, len(array)-1):
    for j in range(1, len(array[i])-1):
        surroundings = get_moore_neighbourhood(i, j)
        if array[i][j] == 1 and sum(surroundings) < 4:
            global_counter += 1

print(f"result 1: {global_counter}")
