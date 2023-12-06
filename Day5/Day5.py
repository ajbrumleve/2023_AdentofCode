def extract_seed_list(line):
    seed_list = line.split(":")[1].strip().split(" ")
    seed_list = [int(x) for x in seed_list]
    return seed_list

def extract_seed_list_2(line):
    final_list = []
    seed_list = line.split(":")[1].strip().split(" ")
    seed_list = [int(x) for x in seed_list]
    for i in range(len(seed_list)):
        if i%2==0:
            seed_no = seed_list[i]
            seed_range = seed_list[i+1]
            final_list.append((seed_no,seed_range))
    return final_list



def process(tuple_arr):
    output_dict = {}
    sorted_list = sorted(tuple_arr, key=lambda x: x[1])
    output_dict[0] = 0
    # key = arr[1]
    # val = arr[0]
    # interval = arr[2]
    # if sorted_list[0][1] == 0:
    #     output_dict[0]=0
    for tuple in sorted_list:
        output_dict[tuple[1]] = tuple[0]
        output_dict[tuple[1] + tuple[2]] = tuple[1] + tuple[2]
    return output_dict

def invert_dictionary(dict_input):
    inverted_dict = {}
    for key, val in dict_input.items():
        inverted_dict[val]=key
    return inverted_dict

def get_val(dictionary_name, input_value):
    value_dict = dictionary_name
    keys = sorted(value_dict.keys())
    last_num = 0
    for num in keys:
        if input_value < num:
            diff = input_value - last_num
            result = value_dict[last_num] + diff
            return result
        else:
            last_num = num
    diff = input_value - last_num
    result = value_dict[last_num] + diff
    return result


def part1(file):
    with (open(file, 'r') as f):
        maps_arr = []
        current_map = ""
        tuple_arr = []
        for line in f:
            # seeds = extract_seed_arr(line)
            if "map" in line:
                current_map = line.strip()

            elif "seeds" in line:
                seed_list = extract_seed_list(line)
            elif line == "\n":
                if len(tuple_arr) > 0:
                    maps_arr.append((current_map, process(tuple_arr)))
                    tuple_arr = []
            else:
                arr = line.strip().split(" ")
                tuple_arr.append((int(arr[0]), int(arr[1]), int(arr[2])))
        if len(tuple_arr) > 0:
            maps_arr.append((current_map, process(tuple_arr)))
            tuple_arr = []
    result_arr = []
    for input_num in seed_list:
        for i in range(7):
            input_num = get_val(maps_arr[i][1], input_num)
        result_arr.append(input_num)

    return min(result_arr)





def part2(file):
    with (open(file, 'r') as f):
        maps_arr = []
        current_map = ""
        tuple_arr = []
        for line in f:
            # seeds = extract_seed_arr(line)
            if "map" in line:
                current_map = line.strip()

            elif "seeds" in line:
                seed_list = extract_seed_list_2(line)


            elif line == "\n":
                if len(tuple_arr) > 0:
                    maps_arr.append((current_map, process(tuple_arr)))
                    tuple_arr = []
            else:
                arr = line.strip().split(" ")
                tuple_arr.append((int(arr[0]), int(arr[1]), int(arr[2])))
        if len(tuple_arr) > 0:
            maps_arr.append((current_map, process(tuple_arr)))
            tuple_arr = []
    i = 0
    break_points = []
    dict = {}
    break_points = list(maps_arr[i][1].keys())

    for j in range(i + 1):
        for item in break_points:
            dict[item] = get_val(maps_arr[i][1], item)

    inverted = invert_dictionary(dict)

    for i in range(1, 7):

        new_break_points = maps_arr[i][1].keys()
        for new_break_point in new_break_points:
            new_break_seed = get_val(inverted, new_break_point)
            break_points.append(new_break_seed)
        break_points = list(set(break_points))
        new_dict = {}
        for seed in break_points:
            input_num = seed
            for k in range(i + 1):
                input_num = get_val(maps_arr[k][1], input_num)
            new_dict[seed] = input_num
            inverted = invert_dictionary(new_dict)

    keys = []
    vals = []
    for key in sorted(new_dict.keys()):
        keys.append(key)
        vals.append(new_dict[key])

    seed_arr = []
    for seed, seed_range in seed_list:
        seed_arr.append(seed)
        seed_breaks = [x for x in keys if x < seed + seed_range and x > seed]
        seed_arr.extend(seed_breaks)

    result_arr = []
    for input_num in seed_arr:
        for i in range(7):
            input_num = get_val(maps_arr[i][1], input_num)
        result_arr.append(input_num)

    return min(result_arr)


answer1 = part1('C:/Users/abrumleve4982/Documents/PycharmProjects/2023AOC/Day5/input')
answer2 = part2('C:/Users/abrumleve4982/Documents/PycharmProjects/2023AOC/Day5/input')

print(f"The first answer is {answer1}")
print(f"The second answer is {answer2}")


