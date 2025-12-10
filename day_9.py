from loaders import load_list_from_lines_no_strip


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

def calculate_rectangle_area(x,y, x2, y2):
    return abs((x2 - x+1) * (y2 - y+1))

cleaned_input = [list(map(int,line.split(","))) for line in input_array]

largest_rectangle_area = 0
for x, y in cleaned_input:
    for x2, y2 in cleaned_input:
        rectangle_area = calculate_rectangle_area(x,y,x2,y2)
        if rectangle_area > largest_rectangle_area:
            largest_rectangle_area = rectangle_area

print(f"result 1: {largest_rectangle_area}")

