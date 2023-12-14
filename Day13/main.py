import math
import time
import re
from collections import Counter
from itertools import groupby

import numpy as np
import sys


def make_np_array(map):
    num_cols = len(map.splitlines()[0])
    num_rows = len(map.splitlines())
    # Remove trailing whitespace from each line
    content = [line.rstrip() for line in map]

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


def find_different_by_one_first_col(matrix):
    # Subtract each column from the first column and count differences
    differences = np.sum(matrix[:, 1:] != matrix[:, 0, None], axis=0)
    # Find columns where there is exactly one difference
    one_difference_columns = np.where((differences == 1) | (differences == 0))[0]
    return (
        one_difference_columns + 1
    )  # Adjust indices to account for zero-based indexing


def find_different_by_one_last_col(matrix):
    # Subtract each column from the first column and count differences
    differences = np.sum(matrix[:, :-1] != matrix[:, -1, None], axis=0)
    # Find columns where there is exactly one difference
    one_difference_columns = np.where((differences == 1) | (differences == 0))[0]
    return one_difference_columns  # Adjust indices to account for zero-based indexing


def find_different_by_one_first_row(matrix):
    # Subtract each column from the first column and count differences
    differences = np.sum(matrix[1:] != matrix[0], axis=1)
    # Find columns where there is exactly one difference
    one_difference_columns = np.where((differences == 1) | (differences == 0))[0]
    return (
        one_difference_columns + 1
    )  # Adjust indices to account for zero-based indexing


def find_different_by_one_last_row(matrix):
    # Subtract each column from the first column and count differences
    differences = np.sum(matrix[:-1] != matrix[-1], axis=1)
    # Find columns where there is exactly one difference
    one_difference_columns = np.where((differences == 1) | (differences == 0))[0]
    return one_difference_columns  # Adjust indices to account for zero-based indexing


def check_first_col(map_arr, part):
    if part == 1:
        identical_columns_indices = (
            np.all(map_arr[:, 1:] == map_arr[:, 0, None], axis=0).nonzero()[0] + 1
        )

    else:
        identical_columns_indices = find_different_by_one_first_col(map_arr)

    if len(identical_columns_indices) == 1:
        comparison = compare_two_cols(map_arr, 0, identical_columns_indices[0], part)
        diff = identical_columns_indices[0]
        if diff % 2 == 1 and comparison:
            number_left = math.floor(np.mean([0, identical_columns_indices[0]])) + 1
        else:
            number_left = 0
        return number_left
    elif len(identical_columns_indices) > 1:
        print("Multiple matches")
        pairs = make_index_pair_arr(identical_columns_indices, 0, map_arr.shape[1] - 1)
        for pair in pairs:
            if compare_two_cols(map_arr, pair[0], pair[1], part):
                number_left = math.floor(np.mean([pair[0], pair[1]])) + 1
                return number_left
        return 0
    else:
        return 0


def check_last_col(map_arr, part):
    if part == 1:
        identical_columns_indices = np.all(
            map_arr[:, :-1] == map_arr[:, -1, None], axis=0
        ).nonzero()[0]
    else:
        identical_columns_indices = find_different_by_one_last_col(map_arr)

    if len(identical_columns_indices) == 1:
        comparison = compare_two_cols(
            map_arr, identical_columns_indices[0], map_arr.shape[1] - 1, part
        )
        diff = map_arr.shape[1] - 1 - identical_columns_indices[0]
        if diff % 2 == 1 and comparison:
            number_left = (
                math.floor(
                    np.mean([map_arr.shape[1] - 1, identical_columns_indices[0]])
                )
                + 1
            )
        else:
            number_left = 0

        return number_left

    elif len(identical_columns_indices) > 1:
        print("Multiple matches")
        pairs = make_index_pair_arr(
            identical_columns_indices, map_arr.shape[1] - 1, map_arr.shape[1] - 1
        )
        for pair in pairs:
            if compare_two_cols(map_arr, pair[0], pair[1], part):
                number_left = math.floor(np.mean([pair[0], pair[1]])) + 1
                return number_left
        return 0
    else:
        return 0


def check_rows(map_arr, part):
    if part == 1:
        diff = 0
    else:
        diff = 1
    first_row_val1 = check_first_row(map_arr, part)
    last_row_val1 = check_last_row(map_arr, part)
    first_row_val = check_from_top(map_arr, diff)
    last_row_val = check_from_bottom(map_arr, diff)
    return max(first_row_val, last_row_val)


def check_first_row(map_arr, part):
    if part == 1:
        identical_rows_indices = (
            np.all(map_arr[1:] == map_arr[0], axis=1).nonzero()[0] + 1
        )
    else:
        identical_rows_indices = find_different_by_one_first_row(map_arr)
    if len(identical_rows_indices) == 1:
        comparison = compare_two_rows(map_arr, 0, identical_rows_indices[0], part)
        diff = identical_rows_indices[0]
        if diff % 2 == 1 and comparison:
            number_above = math.floor(np.mean([0, identical_rows_indices[0]])) + 1
        else:
            number_above = 0
        return number_above
    elif len(identical_rows_indices) > 1:
        print("Multiple matches")
        pairs = make_index_pair_arr(identical_rows_indices, 0, map_arr.shape[0] - 1)
        for pair in pairs:
            if compare_two_rows(map_arr, pair[0], pair[1], part):
                number_above = math.floor(np.mean([pair[0], pair[1]])) + 1
                return number_above
        return 0
    else:
        return 0


def check_last_row(map_arr, part):
    if part == 1:
        identical_rows_indices = np.all(map_arr[:-1] == map_arr[-1], axis=1).nonzero()[
            0
        ]
    else:
        identical_rows_indices = find_different_by_one_last_row(map_arr)
    if len(identical_rows_indices) == 1:
        comparison = compare_two_rows(
            map_arr, identical_rows_indices[0], map_arr.shape[0] - 1, part
        )
        diff = map_arr.shape[0] - 1 - identical_rows_indices[0]
        if diff % 2 == 1 and comparison:
            number_above = (
                math.floor(np.mean([map_arr.shape[0] - 1, identical_rows_indices[0]]))
                + 1
            )
        else:
            number_above = 0
        return number_above
    elif len(identical_rows_indices) > 1:
        print("Multiple matches")
        pairs = make_index_pair_arr(
            identical_rows_indices, map_arr.shape[0] - 1, map_arr.shape[0] - 1
        )
        for pair in pairs:
            if compare_two_rows(map_arr, pair[0], pair[1], part):
                number_above = math.floor(np.mean([pair[0], pair[1]])) + 1
                return number_above
        return 0
    else:
        return 0


def make_index_pair_arr(indices, reference_index, maximum_index):
    pair_list = []
    indices = list(indices)
    indices.append(reference_index)
    indices.sort()
    extremes = [0, maximum_index]
    while len(indices) > 0:
        first_val = indices.pop(0)
        for index in indices:
            while first_val not in extremes and index not in extremes:
                first_val -= 1
                index += 1
            pair_list.append((first_val, index))
    return pair_list


def compare_two_rows(arr, row1_idx, row2_idx, part):
    if part == 1:
        while row1_idx < row2_idx:
            if np.array_equal(arr[row1_idx], arr[row2_idx]):
                row1_idx += 1
                row2_idx -= 1
            else:
                return False
    else:
        count = 0
        while row1_idx < row2_idx:
            rows_diff = np.count_nonzero(arr[row1_idx] != arr[row2_idx])
            if rows_diff < 2 and count < 2:
                row1_idx += 1
                row2_idx -= 1
                count += rows_diff
            else:
                return False
        if count != 1:
            return False
    return True


def compare_two_cols(arr, col1_idx, col2_idx, part):
    if part == 1:
        while col1_idx < col2_idx:
            if np.array_equal(arr[:, col1_idx], arr[:, col2_idx]):
                col1_idx += 1
                col2_idx -= 1
            else:
                return False
    else:
        count = 0
        while col1_idx < col2_idx:
            cols_diff = np.count_nonzero(arr[:, col1_idx] != arr[:, col2_idx])
            if cols_diff < 2 and count < 2:
                col1_idx += 1
                col2_idx -= 1
                count += cols_diff
            else:
                return False
        if count != 1:
            return False
    return True


def check_cols(map_arr, part):
    if part == 1:
        diff = 0
    else:
        diff = 1
    # first_col_val = check_first_col(map_arr, part)
    # last_col_val = check_last_col(map_arr, part)
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
    for map in map_arrs:
        map_arr = make_np_array(map)
        value = get_summary(map_arr, part)
        val += value
    return val


def check_from_left(map_arr, diff):
    for i in range(math.floor(map_arr.shape[1] / 2)):
        diffs = np.count_nonzero(
            map_arr[:, 0 : i + 1] != map_arr[:, i + 1 : (2 * (i + 1))][:, ::-1]
        )
        if diffs == diff:
            return i + 1
    return 0


def check_from_right(map_arr, diff):
    last_index = map_arr.shape[1] - 1
    for i in range(math.floor(map_arr.shape[1] / 2)):
        diffs = np.count_nonzero(
            map_arr[:, last_index - i : last_index + 1]
            != map_arr[:, last_index - 1 - (2 * i) : last_index - i][:, ::-1]
        )
        if diffs == diff:
            return last_index - i

    return 0


def check_from_top(map_arr, diff):
    for i in range(math.floor(map_arr.shape[0] / 2)):
        diffs = np.count_nonzero(
            map_arr[0 : i + 1, :] != map_arr[i + 1 : (2 * (i + 1)), :][::-1, :]
        )
        if diffs == diff:
            return i + 1
    return 0


def check_from_bottom(map_arr, diff):
    last_index = map_arr.shape[0] - 1
    for i in range(math.floor(map_arr.shape[0] / 2)):
        diffs = np.count_nonzero(
            map_arr[last_index - i : last_index + 1, :]
            != map_arr[last_index - 1 - (2 * i) : last_index - i, :][::-1, :]
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
