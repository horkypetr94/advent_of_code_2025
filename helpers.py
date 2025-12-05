def load_list_from_lines(path: str) -> list:
    items = []
    with open(path) as f:
        data = f.readlines()
        for line in data:
            items.append(line.strip())

    return items


def load_str_from_line(path: str) -> str:
    with open(path) as f:
        data = f.readlines()

    return data[0]
