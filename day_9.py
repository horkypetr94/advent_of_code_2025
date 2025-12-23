from tqdm import tqdm

from loaders import load_list_from_lines_no_strip
import numpy as np

input_array = [
    "7,1",
    "11,1",
    "11,7",
    "9,7",
    "9,5",
    "2,5",
    "2,3",
    "7,3",
]
input_array = load_list_from_lines_no_strip("data/day_9_1")


def calculate_rectangle_area(x, y, x2, y2):
    return abs((x2 - x + 1) * (y2 - y + 1))


cleaned_input = [list(map(int, line.split(","))) for line in input_array]

largest_rectangle_area = 0
for x, y in cleaned_input:
    for x2, y2 in cleaned_input:
        rectangle_area = calculate_rectangle_area(x, y, x2, y2)
        if rectangle_area > largest_rectangle_area:
            largest_rectangle_area = rectangle_area

print(f"result 1: {largest_rectangle_area}")

array = np.zeros(shape=(100000, 100000))
for x, y in cleaned_input:
    array[y, x] = 1

for i, line in tqdm(enumerate(array[:])):
    if sum(line) > 1:
        start, stop = np.where(line == 1)[0]
        array[i, start : stop + 1] = 1

for j in range(array.shape[1]):
    col = array[:, j]
    if np.sum(col) > 1:
        indices = np.where(col == 1)[0]
        start = indices[0]
        stop = indices[-1]
        array[start : stop + 1, j] = 1

largest_rectangle = 0
for x, y in tqdm(cleaned_input):
    for x2, y2 in cleaned_input:
        rectangle = np.zeros(shape=(100000, 100000))
        rectangle[y : y2 + 1, x : x2 + 1] = 1
        if np.prod(array[y : y2 + 1, x : x2 + 1]) > 0:
            local_sum = np.sum(rectangle * array)
            if local_sum > largest_rectangle:
                largest_rectangle = local_sum
                # print(x, y, x2, y2)
                # print(largest_rectangle)

print(f"result 2: {largest_rectangle}")
