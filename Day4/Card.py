class Card:

    def __init__(self,id, my_arr, winning_arr):
        self.id = id
        self.num_cards = 1
        self.my_arr = my_arr
        self.winning_arr = winning_arr
        self.combo = set(self.winning_arr).intersection(set(self.my_arr))
