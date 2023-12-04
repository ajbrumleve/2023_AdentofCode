def parse_input(file):
    num_dict_temp = []
    sym_dict_temp = {}
    with open(file, 'r') as f:
        j = 1
        for line in f:
            sym_dict_temp[j] = {}
            number = ""
            previous_char = ""
            first_ind = 0
            for i in range(len(line)):
                char = line[i]
                if char.isnumeric() and i == len(line) - 1:
                    number += char
                    last_ind = i
                    num_dict_temp.append((number, {"first": first_ind, "last": last_ind, "line": j}))
                    previous_char = char
                    first_ind = 0
                    number = 0
                elif char.isnumeric() and previous_char.isnumeric():
                    number += char
                    previous_char = char
                elif char.isnumeric() and not previous_char.isnumeric():
                    number = char
                    first_ind = i
                    previous_char = char
                elif not char.isnumeric() and previous_char.isnumeric():
                    last_ind = i - 1
                    num_dict_temp.append((number, {"first": first_ind, "last": last_ind, "line": j}))
                    previous_char = char
                    first_ind = 0
                    number = 0
                    if char != "." and char != "\n":
                        sym_dict_temp[j][i] = char
                elif not char.isnumeric():
                    if char != "." and char != "\n":
                        sym_dict_temp[j][i] = char
            if len(sym_dict_temp[j]) == 0:
                del sym_dict_temp[j]
            j += 1

    return num_dict_temp, sym_dict_temp


def process_number(number, num_dict, symbol_dict):
    for line in range(num_dict["line"] - 1, num_dict["line"] + 2):
        if line in symbol_dict.keys():
            cols_to_check = range(num_dict["first"] - 1, num_dict["last"] + 2)
            for col in cols_to_check:
                if col in symbol_dict[line].keys():
                    return int(number)
    return 0


def process_number_2(number, num_dict, symbol_dict, gear_dict):
    for line in range(num_dict["line"] - 1, num_dict["line"] + 2):
        if line in symbol_dict.keys():
            cols_to_check = range(num_dict["first"] - 1, num_dict["last"] + 2)
            for col in cols_to_check:
                if col in symbol_dict[line].keys():
                    if symbol_dict[line][col] == "*":
                        gear_dict[(line, col)] = gear_dict.get((line, col), [])
                        gear_dict[(line, col)].append(number)
    return gear_dict


def part1(file):
    val = 0
    num_dict, symbol_dict = parse_input(file)
    for number, num_stats in num_dict:
        # for line in range(num_dict[key]["line"]-1,num_dict[key]["line"]+2):
        #     if line in symbol_dict.keys():
        #         cols_to_check = range(num_dict[key]["first"]-1,num_dict[key]["last"]+2)
        #         for col in cols_to_check:
        #             if col in symbol_dict[line].keys():
        #                 return int(key)
        # return 0
        value = process_number(number, num_stats, symbol_dict)
        val += value

    return val


def part2(file):
    final_val = 0
    gear_dict = {}
    num_dict, symbol_dict = parse_input(file)
    for number, num_stats in num_dict:
        # for line in range(num_dict[key]["line"]-1,num_dict[key]["line"]+2):
        #     if line in symbol_dict.keys():
        #         cols_to_check = range(num_dict[key]["first"]-1,num_dict[key]["last"]+2)
        #         for col in cols_to_check:
        #             if col in symbol_dict[line].keys():
        #                 return int(key)
        # return 0
        gear_dict = process_number_2(number, num_stats, symbol_dict, gear_dict)

    for key, val in gear_dict.items():
        if len(val) == 2:
            int_list = [int(x) for x in val]
            gear_ratio = int_list[0] * int_list[1]
            final_val += gear_ratio

    return final_val


answer1 = part1('input_3')
answer2 = part2('input_3')

print(f"The first answer is {answer1}")
print(f"The second answer is {answer2}")
