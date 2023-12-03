def get_id(line):
    return int(line.split(":")[0].split(" ")[1])


def get_list_sets(line):
    return line.split(":")[1].split(";")


def get_set_dict(input_set):
    set_dict = {"red": 0, "blue": 0, "green": 0}
    list_draws = input_set.split(",")
    for item in list_draws:
        item = item.strip()
        items = item.split(" ")
        set_dict[items[1]] = int(items[0])
    return set_dict


def part1(red, green, blue):
    val = 0
    with open('input_2', 'r') as f:
        for line in f:
            valid = True
            line_id = get_id(line)
            list_sets = get_list_sets(line)
            for puzzle_set in list_sets:
                set_dict = get_set_dict(puzzle_set)
                if set_dict["red"] > red or set_dict["green"] > green or set_dict["blue"] > blue:
                    valid = False
            if valid:
                val += line_id
    return val


def compare_set_dicts(set_dict, new_set_dict):
    new_dict = {}
    for key in set_dict.keys():
        new_dict[key] = max(set_dict[key], new_set_dict[key])
    return new_dict


def part2():
    val = 0
    with (open('input_2', 'r') as f):
        for line in f:
            power = 1
            set_dict = {"red": 0, "blue": 0, "green": 0}
            list_sets = get_list_sets(line)
            for puzzle_set in list_sets:
                new_set_dict = get_set_dict(puzzle_set)
                set_dict = compare_set_dicts(set_dict, new_set_dict)
            for value in set_dict.values():
                power = power * value
            val += power

    return val


answer1 = part1(12,13,14)
answer2 = part2()
