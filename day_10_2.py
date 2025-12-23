from z3 import Sum, sat, Int, Optimize
from loaders import load_list_from_lines_no_strip

input_data = load_list_from_lines_no_strip("data/day_10_1")
total_presses = 0

for line in input_data:
    parts = line.split(" ")
    targets = [int(x) for x in parts[-1].strip().strip("{}").split(",")]
    buttons = []
    for b in parts[1:-1]:
        clean = b.strip("()")
        buttons.append([int(x) for x in clean.split(",")])

    opt = Optimize()
    x = [Int(f"x_{i}") for i in range(len(buttons))]
    for var in x:
        opt.add(var >= 0)
    for c_idx, target_val in enumerate(targets):
        relevant_buttons = []
        for b_idx, btn_indices in enumerate(buttons):
            if c_idx in btn_indices:
                relevant_buttons.append(x[b_idx])
        opt.add(Sum(relevant_buttons) == target_val)
    opt.minimize(Sum(x))
    if opt.check() == sat:
        total_presses += opt.model().eval(Sum(x)).as_long()

print(f"Total Minimum Presses: {total_presses}")
