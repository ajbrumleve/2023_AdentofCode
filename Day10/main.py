import time
from itertools import groupby
import numpy as np
import sys

# Set a new recursion limit
new_recursion_limit = 15000  # Change this to your desired value

sys.setrecursionlimit(new_recursion_limit)
points = []


def parse(file):
    # Read the text file
    with open(file, "r") as f:
        content = f.read()
    num_cols = len(content.splitlines()[0])
    num_rows = len(content.splitlines())
    # Remove trailing whitespace from each line
    content = [line.rstrip() for line in content]

    # Join the lines into a single string
    content = "".join(content)
    # Create a 1D NumPy array from the characters
    array_1d = np.array(list(content))

    # Reshape the array to a 2D array (5x5)
    array_2d = array_1d.reshape((num_rows, num_cols))

    return array_2d


def find_s(arr):
    indices = np.where(arr == "S")
    return indices[0][0], indices[1][0]


def check_up(arr, loc_tup, count):
    try:
        up_val = arr[loc_tup[0] - 1][loc_tup[1]]
        uo_loc = (loc_tup[0] - 1, loc_tup[1])
        points.append((uo_loc[0], uo_loc[1], up_val))
    except:
        return count
    if up_val == "F":
        return check_right(arr, uo_loc, count + 1)
    elif up_val == "7":
        return check_left(arr, uo_loc, count + 1)
    elif up_val == "|":
        return check_up(arr, uo_loc, count + 1)
    elif up_val == "S":
        return count + 1
    else:
        return False


def check_right(arr, loc_tup, count):
    try:
        right_val = arr[loc_tup[0]][loc_tup[1] + 1]
        right_loc = (loc_tup[0], loc_tup[1] + 1)
        points.append((right_loc[0], right_loc[1], right_val))
    except:
        return count
    if right_val == "J":
        return check_up(arr, right_loc, count + 1)
    elif right_val == "7":
        return check_down(arr, right_loc, count + 1)
    elif right_val == "-":
        return check_right(arr, right_loc, count + 1)
    elif right_val == "S":
        return count + 1
    else:
        return False


def check_down(arr, loc_tup, count):
    try:
        down_val = arr[loc_tup[0] + 1][loc_tup[1]]
        down_loc = (loc_tup[0] + 1, loc_tup[1])
        points.append((down_loc[0], down_loc[1], down_val))

    except:
        return count
    if down_val == "L":
        return check_right(arr, down_loc, count + 1)
    elif down_val == "J":
        return check_left(arr, down_loc, count + 1)
    elif down_val == "|":
        return check_down(arr, down_loc, count + 1)
    elif down_val == "S":
        return count + 1
    else:
        return False


def check_left(arr, loc_tup, count):
    try:
        left_val = arr[loc_tup[0]][loc_tup[1] - 1]
        left_loc = (loc_tup[0], loc_tup[1] - 1)
        points.append((left_loc[0], left_loc[1], left_val))

    except:
        return False
    if left_val == "F":
        return check_down(arr, left_loc, count + 1)
    elif left_val == "L":
        return check_up(arr, left_loc, count + 1)
    elif left_val == "-":
        return check_left(arr, left_loc, count + 1)
    elif left_val == "S":
        return count + 1
    else:
        return False


# def check_up2(arr, loc_tup, count):
#     try:
#         up_val = arr[loc_tup[0] - 1][loc_tup[1]]
#         uo_loc = (loc_tup[0]-1,loc_tup[1])
#         points.append((uo_loc[0],uo_loc[1],up_val))
#     except:
#         return count
#     if up_val == "F":
#         return check_right2(arr, uo_loc, count+1)
#     elif up_val == "7":
#         return check_left2(arr, uo_loc, count+1)
#     elif up_val == "|":
#         return check_up2(arr,uo_loc, count+1)
#     elif up_val == "S":
#         return count + 1
#     else:
#         return False
#
# def check_right2(arr, loc_tup, count):
#     try:
#         right_val = arr[loc_tup[0]][loc_tup[1]+1]
#         right_loc = (loc_tup[0],loc_tup[1]+1)
#         points.append((right_loc[0],right_loc[1], right_val))
#     except:
#         return count
#     if right_val == "J":
#         return check_up2(arr, right_loc, count+1)
#     elif right_val == "7":
#         return check_down2(arr, right_loc, count+1)
#     elif right_val == "-":
#         return check_right2(arr,right_loc,count+1)
#     elif right_val == "S":
#         return count + 1
#     else:
#         return False
#
# def check_down2(arr, loc_tup, count):
#     try:
#         down_val = arr[loc_tup[0] + 1][loc_tup[1]]
#         down_loc = (loc_tup[0]+1, loc_tup[1])
#         points.append((down_loc[0],down_loc[1],down_val))
#     except:
#         return count
#     if down_val == "L":
#         return check_right2(arr, down_loc, count+1)
#     elif down_val == "J":
#         return check_left2(arr, down_loc, count+1)
#     elif down_val == "|":
#         return check_down2(arr,down_loc,count+1)
#     elif down_val == "S":
#         return count + 1
#     else:
#         return False
#
# def check_left2(arr, loc_tup, count):
#     try:
#         left_val = arr[loc_tup[0]][loc_tup[1]-1]
#         left_loc = (loc_tup[0], loc_tup[1] - 1)
#         points.append((left_loc[0],left_loc[1],left_val))
#     except:
#         return False
#     if left_val == "F":
#         return check_down2(arr, left_loc, count+1)
#     elif left_val == "L":
#         return check_up2(arr, left_loc, count+1)
#     elif left_val == "-":
#         return check_left2(arr, left_loc, count+1)
#     elif left_val == "S":
#         return count + 1
#     else:
#         return False


def count_dots_in_row(row):
    in_loop = False
    last_turn = ""
    last_col = 0
    count = 0
    for i in range(len(row)):
        element = row[i][2]
        col = row[i][1]
        if last_col != 0:
            num_in_loop = (col - last_col - 1) * in_loop
            count += num_in_loop
        if last_turn == "L" and element == "7":
            in_loop = not in_loop
            last_turn = ""
        elif last_turn == "F" and element == "J":
            in_loop = not in_loop
            last_turn = ""
        elif element == "|":
            in_loop = not in_loop
            last_turn = ""
        elif element == "L":
            last_turn = element
        elif element == "F":
            last_turn = element

        last_col = col
    return count


def process(file, part):
    pipe_map = parse(file)
    s_loc = find_s(pipe_map)
    global points
    points = []
    cond_val = check_right(pipe_map, s_loc, 0)
    if cond_val > 1:
        val = cond_val / 2
    else:
        points = []
        cond_val = check_down(pipe_map, s_loc, 0)
    if cond_val > 1:
        val = cond_val / 2
    else:
        points = []
        cond_val = check_left(pipe_map, s_loc, 0)
        val = cond_val / 2

    if part == 1:
        return val

    if part == 2:
        # points = []
        # check_left2(pipe_map,s_loc,0)
        sorted_points = sorted(points, key=lambda x: (x[0], x[1]))
        grouped_by_row = {
            key: list(group)
            for key, group in groupby(sorted_points, key=lambda x: x[0])
        }

        # Sort each group by column
        final_result = [
            sorted(group, key=lambda x: x[1]) for group in grouped_by_row.values()
        ]

        val = 0
        for row in final_result:
            val += count_dots_in_row(row)
        return val


file = "C:/Users/abrumleve4982/Documents/PycharmProjects/2023AOC/Day10/input"

t0 = time.time()
answer1 = process(
    "C:/Users/abrumleve4982/Documents/PycharmProjects/2023AOC/Day10/input", 1
)
t1 = time.time()
answer2 = process(
    "C:/Users/abrumleve4982/Documents/PycharmProjects/2023AOC/Day10/input", 2
)
t2 = time.time()

print(f"The first answer is {answer1} - Processing time: {t1 - t0}s")
print(f"The second answer is {answer2} - Processing time: {t2 - t1}s")

sys.setrecursionlimit(1000)
