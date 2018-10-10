#tried fom here https://pycarddeck.readthedocs.io/en/latest/examples/poker.html

import pyCardDeck
from pyCardDeck.cards import PokerCard 

# declaring suits and numbers of cards
def initial_deck_cards():
		cards=[]
		suit = ["Hearts","Spades","Clubs","Diamonds"]
		numbers= {'1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine','10':'Ten','J':'Jack','Q':'Queen','K':'King'}

		for item in suit:#looping and appending
			for numbers,name in numbers.items():
				cards.append((item,name))
		print('Generated cards for the table')

class PokerTable:
	
	def __init__(self, players):
		self.players = list(range(1,players))
		self.deck = pyCardDeck.Deck(cards=generate_initial_deck(),name='Poker Game',reshuffle=False)
		self.table_cards=[]
		self.hand = []
		print("This is a poker table with {} players".format(players))


	def texas_holdem(self):
		"""Basic Texas Hold'em game structure"""
		print("Starting a round of Texas Hold'em")
		self.deck.shuffle()
		self.draw_cards(2)
		
	def draw_cards(self, rank):
		card = []
		for _ in range(0, rank):
			for play in self.players:
				card = self.deck.draw()
				play.append(card)
			print("Dealt {} to player {}".format(card, play))

		return cards

print(initial_deck_cards())
PT = PokerTable(5)
print(PT.draw_cards(5))


#-------------------------------second way also tried from other source------

#!/usr/bin/env python3
import collections
import itertools
import random
import pyCardDeck
from pyCardDeck.cards import PokerCard

SUIT_LIST = ("Hearts", "Spades", "Diamonds", "Clubs")
NUMERAL_LIST = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")

class card:
    def __init__(self, numeral, suit):
        self.numeral = numeral
        self.suit = suit
        self.card = self.numeral, self.suit
    def __repr__(self):
        return self.numeral + "-" + self.suit

class poker_hand():
    def __init__(self, card_list):
        self.card_list = card_list
    def __repr__(self):
        short_desc = "Nothing."
        numeral_dict = collections.defaultdict(int)
        suit_dict = collections.defaultdict(int)
        for my_card in self.card_list:
            numeral_dict[my_card.numeral] += 1
            suit_dict[my_card.suit] += 1
        # Pair
        if len(numeral_dict) == 4:
            short_desc = "One pair."
        # Two pair or 3-of-a-kind
        elif len(numeral_dict) == 3:
            if 3 in numeral_dict.values():
                short_desc ="Three-of-a-kind."
            else:
                short_desc ="Two pair."
        # Full house or 4-of-a-kind
        elif len(numeral_dict) == 2:
            if 2 in numeral_dict.values():
                short_desc ="Full house."
            else:
                short_desc ="Four-of-a-kind."
        else:
            # Flushes and straights
            straight, flush = False, False
            if len(suit_dict) == 1:
                flush = True
            min_numeral = min([NUMERAL_LIST.index(x) for x in numeral_dict.keys()])
            max_numeral = max([NUMERAL_LIST.index(x) for x in numeral_dict.keys()])
            if int(max_numeral) - int(min_numeral) == 4:
                straight = True
            # Ace can be low
            low_straight = set(("Ace", "2", "3", "4", "5"))
            if not set(numeral_dict.keys()).difference(low_straight):
                straight = True
            if straight and not flush:
                short_desc ="Straight."
            elif flush and not straight:
                short_desc ="Flush."
            elif flush and  straight:
                short_desc ="Straight flush."
        enumeration = "/".join([str(x) for x in self.card_list])
        return "{enumeration} ({short_desc})".format(**locals())

class deck(set):
    def __init__(self):
        for numeral, suit in itertools.product(NUMERAL_LIST, SUIT_LIST):
            self.add(card(numeral, suit))
    def get_card(self):
        a_card = random.sample(self, 1)[0]
        self.remove(a_card)
        return a_card
    def get_hand(self, number_of_cards=5):
        if number_of_cards == 5:
            return poker_hand([self.get_card() for x in range(number_of_cards)])
        else:
            raise NotImplementedError

for i in range(100):
    print(deck().get_hand())
