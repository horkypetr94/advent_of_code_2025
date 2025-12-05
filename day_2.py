from helpers import load_str_from_line

def task_1(product_ids: list[str]):
    code_counter = 0
    for product_id in product_ids:
        start, end = product_id.split("-")
        int_start = int(start)
        int_end = int(end)

        for code in range(int_start, int_end + 1):
            str_code = str(code)
            code_length = len(str_code)

            if code_length % 2 == 0:
                left_hand, right_hand = (
                    str_code[: code_length // 2],
                    str_code[code_length // 2 :],
                )
                if left_hand == right_hand:
                    code_counter += code

    print(f"The result 1 is: {code_counter}")


def task_2(product_ids: list[str]):
    code_counter = 0
    for product_id in product_ids:
        start, end = product_id.split("-")
        int_start = int(start)
        int_end = int(end)

        for code in range(int_start, int_end + 1):
            str_code = str(code)
            for val in range(1, len(str_code) // 2 + 1):
                code_splits = str_code.split(str_code[:val])
                # find patterns by splitting
                # e.g. "1188511885".split("11885") is ['', '', '']
                if not any(code_splits):
                    code_counter += code
                    # exit loop to prevent from repeating as 2222 would be counted as 2 2 2 2 and 22 22
                    break

    print(f"The result 2 is: {code_counter}")

items = load_str_from_line("data/day_2_1")
product_ids = items.split(",")
task_1(product_ids)
task_2(product_ids)
