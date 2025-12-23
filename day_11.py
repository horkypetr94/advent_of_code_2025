from loaders import load_list_from_lines_no_strip
from tools import reverse_lookup

input = load_list_from_lines_no_strip("data/day_11_1")
# input = [
#     "aaa: you hhh",
#     "you: bbb ccc",
#     "bbb: ddd eee",
#     "ccc: ddd eee fff",
#     "ddd: ggg",
#     "eee: out",
#     "fff: out",
#     "ggg: out",
#     "hhh: ccc fff iii",
#     "iii: out"
# ]

server_dict = {}

for line in input:
    input_val, output_val = line.split(":")
    server_dict[input_val] = output_val.split()


def keys_for_given_values(current_counts: dict) -> dict:
    next_counts = {}
    for value, count in current_counts.items():
        if value in server_dict_lookup:
            found_parents = server_dict_lookup[value]
            for parent in found_parents:
                next_counts[parent] = next_counts.get(parent, 0) + count

    return next_counts


server_dict_lookup = reverse_lookup(server_dict)
current_keys = {"out": 1}
yous = 0

while len(current_keys) > 0:
    current_keys = keys_for_given_values(current_keys)
    if "you" in current_keys:
        yous += current_keys["you"]

print(f"result 1: {yous}")


current_keys = {"svr": 1}
yous = 0
while len(current_keys) > 0:
    current_keys = keys_for_given_values(current_keys)
    if "you" in current_keys:
        yous += current_keys["you"]
print(f"result 2: {yous}")
