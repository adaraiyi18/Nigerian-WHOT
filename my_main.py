import collections import deque

class Game:
    class Card:
        def __init__(self):
            self.shape = ''
            self.number = 0

    class Deck:
        
        def __init__(self, ):
            stack = deque()
            # Flag for error if it reaches above that
            
            
        def donates_to_market(self):
        def flag_offences(self):

        # Checks for plays and then notifies
        def notifies_next_player_special_plays (self):
        def decide_player_turn (self):
        def notifies_next_player_of_special_play(self):
        def suspend(self):


    class Market:

        def __init__(self, cards):
            # cards is a deck of 54
            stack = deque(cards)

        # my_dq is a deque of cards
        def sharing_cards (self, my_dq, no_of_players,):
            
        def receives_cards_from_deck(self):
        def sharing_to_players (self):
        def sharing_to_players_special_plays (self):

    class Player:
        def __init__(self, max_per_person):
            stack = deque()
            while (stack.len() < max_per_person):
                self.pick_from_market()

        def play_card (self, card_no, card_shape):
            for item in self.stack:
                if (card_no == item.number and card_shape == item.shape):
                    return item
            return -1
        
        # receives a list of cards to stack
        def stacking_cards (self, my_list):
            return_list = []
            for item in self.stack:
                if (item.number == my_list[] and item.shape == my_list[]):
                    return_list.append(item)
            return return_list

        def call_semi_last_card (self):
            print("Semi Last Card!")

        def call_last_card (self):
            print("Last Card!")

        def pick_from_market (self, market_dq):
            picking = market_dq.pop()
            self.stack.append(picking)

        def show_cards(self):
            print(self.stack)


    def __init__ (self, number_of_players, card_per_person):
        self.number_of_players = number_of_players
        self.card_per_person = card_per_person

    def get_number_of_player(self):
        return self.number_of_players
    
    def get_cards_per_person(self):
        return self.card_per_person
    
    def create_cards(self,):
        for i in range(54):

        for circles:
        for triangles:
        for crosses:
        for squares:
        for stars:


first_game = Game(5,5)
    
