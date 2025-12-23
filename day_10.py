from itertools import combinations

from loaders import load_list_from_lines_no_strip

input = [
    "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
    "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
    "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}",
]

input = load_list_from_lines_no_strip("data/day_10_1")


def target_to_binary(target: str) -> str:
    binary_str = ""
    for char in target:
        if char == "#":
            binary_str += "1"
        elif char == ".":
            binary_str += "0"
    return binary_str


def switch_to_binary(switches: list[str], target_length: int) -> list:
    all_switches = []
    for switch in switches:
        b_light = list("0" * target_length)
        for light in switch:
            if light.isdigit():
                b_light[int(light)] = "1"
        all_switches.append(int("".join(b_light), 2))

    return all_switches


def apply_xor(b_target: int, b_switches: list[int], len_target: int):
    for r in range(1, len_target + 1):
        for combo in combinations(b_switches, r):
            current_xor = 0
            for val in combo:
                current_xor ^= val
                if b_target == current_xor:
                    return r
    return 0


total_sum = 0
for line in input:
    splitted_line = line.split(" ")
    target, switches = splitted_line[0], splitted_line[1:-1]
    b_targets = target_to_binary(target)
    len_targets = len(b_targets)
    b_switches = switch_to_binary(switches, len_targets)
    result = apply_xor(int(b_targets, 2), b_switches, len_targets)
    print(result)
    total_sum += result
