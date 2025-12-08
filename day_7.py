from loaders import load_list_from_lines_no_strip
lines = [
".......|.......",
"...............",
".......^.......",
"...............",
"......^.^......",
"...............",
".....^.^.^.....",
"...............",
"....^.^...^....",
"...............",
"...^.^...^.^...",
"...............",
"..^...^.....^..",
"...............",
".^.^.^.^.^...^.",
"...............",
]

# lines = load_list_from_lines_no_strip("data/day_7_1")
DOT_CHAR = "."
CARET_CHAR = "^"
BAR_CHAR = "|"

counter = 0
previous = list(lines[0])
for i in range(1, len(lines)):
    current = list(lines[i])
    for j in range(len(previous)):
        if current[j] == DOT_CHAR and previous[j] == BAR_CHAR:
            current[j] = BAR_CHAR
        elif current[j] == CARET_CHAR and previous[j] == BAR_CHAR:
            current[j-1] = BAR_CHAR
            current[j+1] = BAR_CHAR
            counter += 1
        else:
            continue
    previous = current
    print(current)
print(counter)
