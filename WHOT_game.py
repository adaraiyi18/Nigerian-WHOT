from collections import deque
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

class Card:
    def __init__(self):
        self.number = 0
        self.shape = ''
        self.special_ability = ''

    def set_number(self, no):
        self.number = no

    def set_shape(self, shape):
        self.shape = shape

    def set_special_ability(self, sa):
        self.special_ability = sa

    def get_no(self):
        return self.number
    
    def get_shape(self):
        return self.shape
    
    def get_sa(self):
        return self.special_ability

class Market:
    def __init__(self):
        self.created_deck = []
        
        shapes = ['Circle', 'Squares', 'Stars', 'Triangles', 'Crosses']
        numbers = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14]

        for num in numbers:
            for shape in shapes:
                card_obj = Card()
                card_obj.set_number(num)
                card_obj.set_shape(shape)
                if num == 1:
                    card_obj.set_special_ability('Anything')
                elif num == 2:
                    card_obj.set_special_ability('Pick 2')
                elif num == 5:
                    card_obj.set_special_ability('Pick 3')
                elif num == 8:
                    card_obj.set_special_ability('Suspension')
                elif num == 14:
                    card_obj.set_special_ability('General Market')
                self.created_deck.append(card_obj)

        for _ in range(5):
            card_obj = Card()
            card_obj.set_number(20)
            card_obj.set_shape('Whot!')
            card_obj.set_special_ability('Whot-card')
            self.created_deck.append(card_obj)

class Deck:
    def __init__(self):
        self.stack = []

    def logic(self):
        return True

# number of players decided
players_names = ['Alice', 'Derek', 'Job']

players = {name : Player(name) for name in players_names}

my_market = Market()

for name, obj in players.items():
    for i in range(5):
        obj.hand.append(my_market.created_deck.pop())

my_deck = Deck()
my_deck.stack.append(my_market.created_deck.pop())

print(players['Alice'].hand)

# Player 1 plays on deck
my_deck.stack.append(players['Alice'].hand.pop())

# Move is verified as correct

print(players['Alice'].hand)

print(players['Derek'].hand)

# Player 2 plays on deck
my_deck.stack.append(players['Derek'].hand.pop())

# Move is verified as correct

print(players['Derek'].hand)
