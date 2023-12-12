import time
from itertools import groupby

import numpy as np
import sys



def parse(file):
    # Read the text file
    with open(file, 'r') as f:
        content = f.read()
    num_cols = len(content.splitlines()[0])
    num_rows = len(content.splitlines())
    # Remove trailing whitespace from each line
    content = [line.rstrip() for line in content]

    # Join the lines into a single string
    content = ''.join(content)
    # Create a 1D NumPy array from the characters
    array_1d = np.array(list(content))

    # Reshape the array to a 2D array (5x5)
    array_2d = array_1d.reshape((num_rows, num_cols))

    return array_2d

def insert_rows(arr):

    iter_factor= 0
    # Insert new rows
    for i in range(arr.shape[0]):
        if all(arr[i+iter_factor] == '.'):
            arr = np.insert(arr, i+iter_factor, '.', axis=0)
            iter_factor+=1
    return arr

def insert_rows2(arr, num_rows_to_insert):
    # Create a row of dots
    row_of_dots = np.full(arr.shape[1], '.', dtype=arr.dtype)

    # Repeat the row_of_dots to create the new rows
    new_rows = np.tile(row_of_dots, (num_rows_to_insert, 1))



    return new_rows

def insert_cols(arr):
    iter_factor = 0
    # Insert new columns
    for j in range(arr.shape[1]):
        if all(arr[:, j+iter_factor] == '.'):
            arr = np.insert(arr, j+iter_factor, '.', axis=1)
            iter_factor += 1
    return arr

def update_row_locs(arr,locs,num_inserts):
    factor=0
    for i in range(arr.shape[0]):
        if all(arr[i] == '.'):
            locs[locs[:,0]>(i+factor), 0] += num_inserts
            factor+=num_inserts
    return locs

def update_col_locs(arr,locs,num_inserts):
    factor=0
    for j in range(arr.shape[1]):
        if all(arr[:,j] == '.'):
            locs[locs[:,1]>(j+factor), 1] += num_inserts
            factor += num_inserts
    return locs


def get_locations(arr, symbol):
    hash_indices = np.argwhere(arr == symbol)
    return hash_indices

def process(file,part):
    map = parse(file)
    if part == 1:
        num_inserts = 1
    elif part == 2:
        num_inserts = 999999

    locations = get_locations(map, "#")
    locations = update_row_locs(map, locations, num_inserts)
    locations = update_col_locs(map, locations, num_inserts)

    val = 0
    while locations.size > 0:
        loc_to_process = locations[0]
        locations = np.delete(locations,0,axis=0)
        for location in locations:
            dist = abs(loc_to_process[0]-location[0])+abs(loc_to_process[1]-location[1])
            val += dist
    return val






t0 = time.time()
answer1 = process('C:/Users/abrumleve4982/Documents/PycharmProjects/2023AOC/Day11/input', 1)
t1 = time.time()
answer2 = process('C:/Users/abrumleve4982/Documents/PycharmProjects/2023AOC/Day11/input', 2)
t2 = time.time()

print(f"The first answer is {answer1} - Processing time: {t1 - t0}s")
print(f"The second answer is {answer2} - Processing time: {t2 - t1}s")

