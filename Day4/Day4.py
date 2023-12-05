import numpy as np

from Card import Card
import matplotlib.pyplot as plt
def visualize_part_2(arr_cards, visualization):


    # Extracting the values of 'num_cards'
    num_cards_values = [obj.num_cards for obj in arr_cards]
    # Calculating the cumulative sum
    cumulative_sum = np.cumsum(num_cards_values)

    if visualization=="bar":
        # Creating a bar chart
        plt.bar(range(len(num_cards_values)), num_cards_values,
                tick_label=[str(i) for i in range(1, len(num_cards_values) + 1)])
        plt.xlabel('Object Index')
        plt.ylabel('num_cards Value')
        plt.title('Bar Chart of num_cards Values for Each Object')
        plt.show(block=False)
    if visualization == "cumulative":
        # Creating a bar chart for the cumulative sum
        plt.bar(range(1, len(cumulative_sum) + 1), cumulative_sum)
        plt.xlabel('Object Index')
        plt.ylabel('Cumulative Sum of num_cards')
        plt.title('Cumulative Sum Chart of num_cards Values')
        plt.draw()
        plt.show(block=False)
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


    return final_val


def part2(file, visualization=None):
    final_val = 0
    cards = []
    with open(file, 'r') as f:
        i = 1
        for line in f:
            val = 0
            winning_str, our_str = line.split("|")
            winning_str = winning_str.replace("  ", " ")
            our_str = our_str.replace("  ", " ")
            winning_str = winning_str.split(":")[1]
            winning_arr = winning_str.strip().split(" ")
            our_arr = our_str.strip().split(" ")
            card = Card(i,our_arr,winning_arr)
            cards.append(card)
            i+=1
    for i in range(len(cards)):
        card_to_process = cards[i]
        matches = len(card_to_process.combo)
        for j in range(matches):
            cards[i+j+1].num_cards += card_to_process.num_cards
        final_val += card_to_process.num_cards


    visualize_part_2(cards,visualization)


    return final_val


answer1 = part1('C:/Users/abrumleve4982/Documents/PycharmProjects/2023AOC/Day4/input')
answer2 = part2('C:/Users/abrumleve4982/Documents/PycharmProjects/2023AOC/Day4/input',"cumulative")

print(f"The first answer is {answer1}")
print(f"The second answer is {answer2}")

