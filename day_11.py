from loaders import load_list_from_lines_no_strip

input = [
    "aaa: you hhh",
    "you: bbb ccc",
    "bbb: ddd eee",
    "ccc: ddd eee fff",
    "ddd: ggg",
    "eee: out",
    "fff: out",
    "ggg: out",
    "hhh: ccc fff iii",
    "iii: out"
]
# input = load_list_from_lines_no_strip("data/day_11_1")
server_dict = {}

for line in input:
    input_val, output_val = line.split(":")
    server_dict[input_val] = output_val.split()

def keys_for_given_values(given_values: list) -> list:
    current_keys = []
    for given_value in given_values:
        for key, line in server_dict.items():
            if given_value in line:
                current_keys.append(key)
    return current_keys


all_valid_values = ["out"]
current_keys = ["out"]
yous = 0
while len(current_keys) > 0:
    current_keys = keys_for_given_values(current_keys)
    yous += current_keys.count("you")
    all_valid_values.extend(current_keys)
    all_valid_values = list(set(all_valid_values))
print(yous)






