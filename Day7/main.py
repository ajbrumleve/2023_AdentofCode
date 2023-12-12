import math
import time

from Day7.Hand import Hand


def parse_file(file, hand_class, part):
    with open(file, 'r') as f:
        for line in f:
            input_str_bet = line.split(" ")[1].strip()
            input_str_card = line.split(" ")[0].strip()
            card_tuple = (input_str_card, input_str_bet)
            if part == 2:
                hand_class.filter_2(card_tuple)
            else:
                hand_class.filter(card_tuple)


def part1(file, part):
    val = 0
    hand = Hand()
    parse_file(file, hand, part)
    hand.combine_and_sort(part)
    hands = hand.sorted_hand
    i = 1
    while len(hands) > 0:
        card = hands.pop()
        val += int(card[1]) * i
        i += 1
    return val



t0 = time.time_ns()
answer1 = part1('C:/Users/abrumleve4982/Documents/PycharmProjects/2023AOC/Day7/input',1)
t1 = time.time_ns()
answer2 = part1('C:/Users/abrumleve4982/Documents/PycharmProjects/2023AOC/Day7/input',2)
t2 = time.time_ns()


print(f"The first answer is {answer1} - Processing time: {t1 - t0}ns")
print(f"The second answer is {answer2} - Processing time: {t1-t0}ns")
