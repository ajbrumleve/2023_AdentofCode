def get_first_digit(input_String):
    pass


def get_second_digit(line):
    pass

def get_digits(input_string):
    dig_list = []
    for char in input_string:
        try:
            int_char = int(char)
            dig_list.append(int_char)
        except:
            continue
    return dig_list


def dig_combine(dig1, dig2):

    return int(str(dig1)+str(dig2))

def map_digs(line):
    list_digs = []
    nums = ["1","2","3",'4','5','6','7','8','9','0']
    map = {"one": "1",
           "two": "2",
           "three": "3",
           "four": "4",
           "five": "5",
           "six": "6",
           "seven": "7",
           "eight": "8",
           "nine": "9"}
    for i in range(len(line)):
        if line[i] in nums:
            list_digs.append(line[i])
        elif line[i:i+3] in map.keys():
            list_digs.append(map[line[i:i+3]])
        elif line[i:i+4] in map.keys():
            list_digs.append(map[line[i:i+4]])
        elif line[i:i+5] in map.keys():
            list_digs.append(map[line[i:i+5]])
    return list_digs

    
def part1():
    sum_nums = 0
    with open('input_1', 'r') as f:
        for line in f:
            digs = get_digits(line)
            dig1 = digs[0]
            dig2 = digs[-1]
            num = dig_combine(dig1, dig2)
            sum_nums += num

    return sum_nums

def part2():
    sum_nums = 0
    with open('input_1', 'r') as f:
        for line in f:
            print(line)
            line = map_digs(line)
            digs = get_digits(line)
            dig1 = digs[0]
            dig2 = digs[-1]
            num = dig_combine(dig1, dig2)
            print(line)
            print(num)
            sum_nums += num

    return sum_nums

answer1 = part1()
answer2 = part2()

