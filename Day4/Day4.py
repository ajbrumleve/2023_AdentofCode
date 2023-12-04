


def part1(file):
    final_val = 0
    with open(file, 'r') as f:

        for line in f:
            val = 0
            winning_str, our_str = line.split("|")
            winning_str = winning_str.replace("  "," ")
            our_str = our_str.replace("  "," ")
            winning_str = winning_str.split(":")[1]
            winning_arr = winning_str.strip().split(" ")
            our_arr = our_str.strip().split(" ")
            winning_set = set(winning_arr)
            our_set = set(our_arr)
            combined = winning_set.intersection(our_set)
            if len(winning_set) != len( winning_arr):
                print("winning Number Difference")
            if len(our_set) != len(our_arr):
                print("our Number Difference")
            if len(combined)>0:
                val = 2**(len(combined)-1)
            final_val+=val
            print(val)

    return final_val


def part2(file):
    final_val = 0


    return final_val


answer1 = part1('D:/PycharmProjects/2023_AdentofCode/Day4/input')
# answer2 = part2('../input_3')

print(f"The first answer is {answer1}")
# print(f"The second answer is {answer2}")
