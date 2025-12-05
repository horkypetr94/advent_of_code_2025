from loaders import load_list_from_lines

lines = load_list_from_lines("data/day_3_1")


def find_highest_number_from_line(line: str, offset: int) -> tuple[int, int]:
    digits = list(map(int, line))
    highest_number = max(digits)
    # Returns the index of the first element with the specified value
    highest_rel_index = digits.index(highest_number)

    return highest_number, highest_rel_index + offset + 1


def calculate_total_joltage(input_lines: list[str], num_cycles: int) -> int:
    joltage_counter = 0
    for input_line in input_lines:
        joltage_number_string = ""
        highest_index = -1

        for num_cycle in range(num_cycles - 1, -1, -1):
            end = -num_cycle if num_cycle > 0 else None
            sub_line = input_line[highest_index + 1 : end]
            highest, highest_index = find_highest_number_from_line(
                sub_line, highest_index
            )
            joltage_number_string += str(highest)

        joltage_counter += int(joltage_number_string)

    return joltage_counter


joltage = calculate_total_joltage(lines, 2)
print(f"Result 1: {joltage}")

joltage = calculate_total_joltage(lines, 12)
print(f"Result 2: {joltage}")
