import time


def parse(line):
    arr = [int(x) for x in line.strip().split()]
    return arr


def drill_down(int_arr):
    new_arr = []
    for i in range(1, len(int_arr)):
        diff = int_arr[i] - int_arr[i - 1]
        new_arr.append(diff)
    return new_arr


def getLevels(line):
    levels = []
    last_level = False
    int_arr = parse(line)
    levels.append(int_arr)
    next_arr = drill_down(int_arr)
    levels.append(next_arr)
    while last_level == False:
        next_arr = drill_down(next_arr)
        levels.append(next_arr)
        if len(set(next_arr)) == 1:
            last_level = True
    return levels


def get_extrapolated_val(line):
    levels = getLevels(line)
    while len(levels)>1:
        last_level = levels.pop()
        last_val = levels[-1][-1]
        levels[-1].append(last_val+last_level[-1])

    return levels[0][-1]

def get_extrapolated_val2(line):
    levels = getLevels(line)
    while len(levels)>1:
        last_level = levels.pop()
        first_val = levels[-1][0]
        levels[-1].insert(0,first_val-last_level[0])

    return levels[0][0]


def part1(file,part):
    val = 0
    with open(file, 'r') as f:
        for line in f:
            if part == 1:
                extr_val = get_extrapolated_val(line)
            elif part == 2:
                extr_val = get_extrapolated_val2(line)

            val += extr_val
    return val


t0 = time.time()
answer1 = part1('C:/Users/abrumleve4982/Documents/PycharmProjects/2023AOC/Day9/input',1)
t1 = time.time()
answer2 = part1('C:/Users/abrumleve4982/Documents/PycharmProjects/2023AOC/Day9/input', 2)
t2 = time.time()

print(f"The first answer is {answer1} - Processing time: {t1 - t0}s")
print(f"The second answer is {answer2} - Processing time: {t2 - t1}s")

file = 'C:/Users/abrumleve4982/Documents/PycharmProjects/2023AOC/Day9/test_input'
