import math
import time


def quadratic_formula(a, b, c):
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    if x1.is_integer():
        x1 += 1
    if x2.is_integer():
        x2 -= 1
    return math.ceil(x1), math.floor(x2)


def parse_file(file):
    result = []
    with open(file, 'r') as f:
        for line in f:
            input_str_arr = line.split(":")[1].strip().split()
            input_int_arr = [int(x) for x in input_str_arr]
            result.append(input_int_arr)
    return result[0], result[1]


def part1(file):
    l1, l2 = parse_file(file)
    val = 1
    while len(l2) > 0:
        x1, x2 = quadratic_formula(-1, l1.pop(), -(l2.pop()))
        val = val * (x2 - x1 + 1)
    return val


def combine_vals(arr):
    comb_str = ""
    for val in arr:
        comb_str = comb_str + str(val)
    comb_int = int(comb_str)
    new_list = [comb_int]
    return new_list


def part2(file):
    l1, l2 = parse_file(file)
    l1 = combine_vals(l1)
    l2 = combine_vals(l2)
    val = 1
    while len(l2) > 0:
        x1, x2 = quadratic_formula(-1, l1.pop(), -(l2.pop()))
        val = val * (x2 - x1 + 1)
    return val

t0 = time.time_ns()
answer1 = part1('C:/Users/abrumleve4982/Documents/PycharmProjects/2023AOC/Day6/input')
t1 = time.time_ns()
answer2 = part2('C:/Users/abrumleve4982/Documents/PycharmProjects/2023AOC/Day6/input')
t2 = time.time_ns()


print(f"The first answer is {answer1} - Processing time: {t1-t0}ns")
print(f"The second answer is {answer2} - Processing time: {t1-t0}ns")

