import math
import time

import numpy as np


def make_np_array(input_map):
    num_cols = len(input_map.splitlines()[0])
    num_rows = len(input_map.splitlines())
    # Remove trailing whitespace from each line
    content = [line.rstrip() for line in input_map]

    # Join the lines into a single string
    content = "".join(content)
    # Create a 1D NumPy array from the characters
    array_1d = np.array(list(content))

    # Reshape the array to a 2D array (5x5)
    array_2d = array_1d.reshape((num_rows, num_cols))

    return array_2d


def parse(file):
    # Read the text file
    with open(file, "r") as f:
        content = f.read()
    map_arrs = content.split("\n\n")
    return map_arrs


def check_rows(map_arr, part):
    if part == 1:
        diff = 0
    else:
        diff = 1

    first_row_val = check_from_top(map_arr, diff)
    last_row_val = check_from_bottom(map_arr, diff)
    return max(first_row_val, last_row_val)


def check_cols(map_arr, part):
    if part == 1:
        diff = 0
    else:
        diff = 1
    first_col_val = check_from_left(map_arr, diff)
    last_col_val = check_from_right(map_arr, diff)

    return max(first_col_val, last_col_val)


def get_summary(map_arr, part):
    row_val = check_rows(map_arr, part) * 100
    col_val = check_cols(map_arr, part)
    return max(row_val, col_val)


def process(file, part):
    val = 0
    map_arrs = parse(file)
    for input_map in map_arrs:
        map_arr = make_np_array(input_map)
        value = get_summary(map_arr, part)
        val += value
    return val


def check_from_left(map_arr, diff):
    for i in range(math.floor(map_arr.shape[1] / 2)):
        diffs = np.count_nonzero(
            map_arr[:, 0: i + 1] != map_arr[:, i + 1: (2 * (i + 1))][:, ::-1]
        )
        if diffs == diff:
            return i + 1
    return 0


def check_from_right(map_arr, diff):
    last_index = map_arr.shape[1] - 1
    for i in range(math.floor(map_arr.shape[1] / 2)):
        diffs = np.count_nonzero(
            map_arr[:, last_index - i: last_index + 1]
            != map_arr[:, last_index - 1 - (2 * i): last_index - i][:, ::-1]
        )
        if diffs == diff:
            return last_index - i

    return 0


def check_from_top(map_arr, diff):
    for i in range(math.floor(map_arr.shape[0] / 2)):
        diffs = np.count_nonzero(
            map_arr[0: i + 1, :] != map_arr[i + 1: (2 * (i + 1)), :][::-1, :]
        )
        if diffs == diff:
            return i + 1
    return 0


def check_from_bottom(map_arr, diff):
    last_index = map_arr.shape[0] - 1
    for i in range(math.floor(map_arr.shape[0] / 2)):
        diffs = np.count_nonzero(
            map_arr[last_index - i: last_index + 1, :]
            != map_arr[last_index - 1 - (2 * i): last_index - i, :][::-1, :]
        )
        if diffs == diff:
            return last_index - i
    return 0


t0 = time.time()
answer1 = process(
    "C:/Users/abrumleve4982/Documents/PycharmProjects/2023AOC/Day13/test_input", 1
)
t1 = time.time()
answer2 = process(
    "C:/Users/abrumleve4982/Documents/PycharmProjects/2023AOC/Day13/input", 1
)
t2 = time.time()
answer3 = process(
    "C:/Users/abrumleve4982/Documents/PycharmProjects/2023AOC/Day13/test_input", 2
)
t3 = time.time()
answer4 = process(
    "C:/Users/abrumleve4982/Documents/PycharmProjects/2023AOC/Day13/input", 2
)
t4 = time.time()

print(f"The first answer is {answer1} - Processing time: {t1 - t0}s")
print(f"The second answer is {answer2} - Processing time: {t2 - t1}s")
print(f"The third answer is {answer3} - Processing time: {t3 - t2}s")
print(f"The fourth answer is {answer4} - Processing time: {t4 - t3}s")
