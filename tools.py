def remap_lol_values(lol, mapping):
    return [[mapping[c] for c in row] for row in lol]


def pad_lol_with_zeros(lol, pad=1):
    rows, cols = len(lol), len(lol[0])
    padded = [[0] * (cols + 2 * pad)]
    padded += [[0] * pad + row + [0] * pad for row in lol]
    padded += [[0] * (cols + 2 * pad)]
    return padded


moore_neighbourhood_dict = {
    "NW": (-1, -1),
    "N": (-1, 0),
    "NE": (-1, 1),
    "W": (0, -1),
    "E": (0, 1),
    "SW": (1, -1),
    "S": (1, 0),
    "SE": (1, 1),
}


def get_moore_neighbourhood(array, line, item):
    items = []
    for diff in moore_neighbourhood_dict.values():
        items.append(array[line + diff[0]][item + diff[1]])
    return items
