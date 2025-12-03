from helpers import create_list_from_lines

lines = create_list_from_lines("data/day_3_1")

def find_highest_number_from_line(line: str, offset:int) -> tuple[int, int]:
    highest_number = 0
    highest_number_index = 0

    for index, char in enumerate(line):
        if int(char) > highest_number:
            highest_number = int(char)
            highest_number_index = index

    return highest_number, highest_number_index + offset + 1


def calculate_total_joltage(input_lines: list[str], num_cycles = int) -> int:
    joltage_counter = 0
    for input_line in input_lines:
        joltage_number_string = ""
        highest_index = -1

        for num_cycle in range(num_cycles-1, -1, -1 ):
            if num_cycle > 0:
                sub_line = input_line[highest_index + 1:-num_cycle]
            else:
                sub_line = input_line[highest_index + 1:]
            highest, highest_index = find_highest_number_from_line(sub_line, highest_index)
            joltage_number_string += str(highest)

        joltage_counter += int(joltage_number_string)

    return joltage_counter


joltage = calculate_total_joltage(lines, 2)
print(f"Result 1: {joltage}")

joltage = calculate_total_joltage(lines, 12)
print(f"Result 2: {joltage}")


