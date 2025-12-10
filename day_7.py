from loaders import load_list_from_lines_no_strip
from datetime import datetime

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

lines = load_list_from_lines_no_strip("data/day_7_1")
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
            current[j - 1] = BAR_CHAR
            current[j + 1] = BAR_CHAR
            counter += 1
        else:
            continue
    print(current)
    previous = current


rows = len(lines)
cols = len(lines[0])
timeline_counts = [0] * cols

for i, char in enumerate(lines[0]):
    if char == 'S' or char == '|':
        timeline_counts[i] = 1

for r in range(1, rows):
    current_row_chars = lines[r]
    next_timeline_counts = [0] * cols

    for c in range(cols):
        if timeline_counts[c] > 0:
            char = current_row_chars[c]
            if char == CARET_CHAR:
                if c - 1 >= 0:
                    next_timeline_counts[c - 1] += timeline_counts[c]
                if c + 1 < cols:
                    next_timeline_counts[c + 1] += timeline_counts[c]
            else:
                next_timeline_counts[c] += timeline_counts[c]

    timeline_counts = next_timeline_counts
    print(timeline_counts)

total_timelines = sum(timeline_counts)
print(f"result 2: {total_timelines}")

