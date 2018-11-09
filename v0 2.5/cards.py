import random
class Card:
    def __init__(self, rank_id, suit_id):
        self.rank_id = rank_id
        self.suit_id = suit_id
        if self.suit_id == 1:
            self.suit = "Spades"
        elif self.suit_id == 2:
            self.suit = "Hearts"
        elif self.suit_id == 3:
            self.suit = "Clubs"
        elif self.suit_id == 4:
            self.suit = "Diamonds"
        else:
            self.suit = "SuitError"

        if self.rank_id == 1:
            self.rank = "Ace"
        elif self.rank_id == 11:
            self.rank = "Jack"
        elif self.rank_id == 12:
            self.rank = "Queen"
        elif self.rank_id == 13:
            self.rank = "King"
        elif self.rank_id == 14:
            self.rank = "Ace"
        elif self.rank_id <= 10 and self.rank_id >= 2:
            self.rank = str(self.rank_id)
        else:
            self.rank = "RankError"
    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)

class Deck:
    def __init__(self):
        self.cards = []
        for a in range(1,5):
            for b in range(2,15):
                self.cards.append(Card(b, a))
    def shuffle(self):
        random.shuffle(self.cards)
    def draw(self, num = 1):
        result = []
        for i in range(num):
            result.append(self.cards.pop())
        return result
