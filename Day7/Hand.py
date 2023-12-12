import statistics as st


class Hand:
    def __init__(self):
        self.sorted_hand = []
        self.five = []
        self.four = []
        self.full = []
        self.three = []
        self.two_pair = []
        self.one_pair = []
        self.high = []
        self.alphabet = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
        self.alphabet2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

    def sort(self, arr, part):
        if len(arr)!=0:
            if part == 2:
                sorted_arr = sorted(arr, key=lambda word: [self.alphabet2.index(c) for c in word[0]])
            else:
                sorted_arr = sorted(arr, key=lambda word: [self.alphabet.index(c) for c in word[0]])
        else:
            sorted_arr = []
        return sorted_arr

    def filter(self, card_tup):
        card_value = card_tup[0]
        used_values = []
        most_freq = st.mode(card_value)
        num_most_freq = card_value.count(most_freq)
        num_vals = len(set(card_value))

        if num_most_freq == 5:
            self.five.append(card_tup)
        elif num_most_freq == 4:
            self.four.append(card_tup)
        elif num_most_freq == 3 and num_vals == 2:
            self.full.append(card_tup)
        elif num_most_freq == 3 and num_vals == 3:
            self.three.append(card_tup)
        elif num_most_freq == 2 and num_vals == 3:
            self.two_pair.append(card_tup)
        elif num_most_freq == 2 and num_vals == 4:
            self.one_pair.append(card_tup)
        elif num_most_freq == 1:
            self.high.append(card_tup)

    def filter_2(self, card_tup):
        card_value = card_tup[0]
        j_count = card_value.count("J")
        card_value = [x for x in card_value if x!="J"]
        try:
            most_freq = st.mode(card_value)
            num_most_freq = card_value.count(most_freq)
        except:
            num_most_freq = 0
        num_vals = len(set(card_value))
        num_most_freq += j_count

        if num_most_freq == 5:
            self.five.append(card_tup)
        elif num_most_freq == 4:
            self.four.append(card_tup)
        elif num_most_freq == 3 and num_vals == 2:
            self.full.append(card_tup)
        elif num_most_freq == 3 and num_vals == 3:
            self.three.append(card_tup)
        elif num_most_freq == 2 and num_vals == 3:
            self.two_pair.append(card_tup)
        elif num_most_freq == 2 and num_vals == 4:
            self.one_pair.append(card_tup)
        elif num_most_freq == 1:
            self.high.append(card_tup)

    def combine_and_sort(self, part):
        final_arr = []
        final_arr.extend(self.sort(self.five,part))
        final_arr.extend(self.sort(self.four,part))
        final_arr.extend(self.sort(self.full,part))
        final_arr.extend(self.sort(self.three,part))
        final_arr.extend(self.sort(self.two_pair,part))
        final_arr.extend(self.sort(self.one_pair,part))
        final_arr.extend(self.sort(self.high,part))
        self.sorted_hand = final_arr
