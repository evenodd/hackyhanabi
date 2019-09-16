from card import Card
from colour import Colour
from game_over_exception import GameOverException
import random
from pybrain.utilities import fListToString

class Deck(object) :
	def __init__(self) :
		self.cards = []
		for colour, member in Colour.__members__.items() :
			self.cards.append(Card(colour, 1))
			self.cards.append(Card(colour, 1))
			self.cards.append(Card(colour, 1))
			self.cards.append(Card(colour, 2))
			self.cards.append(Card(colour, 2))
			self.cards.append(Card(colour, 3))
			self.cards.append(Card(colour, 3))
			self.cards.append(Card(colour, 4))
			self.cards.append(Card(colour, 4))
			self.cards.append(Card(colour, 5))
		# random.Random(4).shuffle(self.cards)
		random.shuffle(self.cards)
		# print(str.join(",", [str(c) for c in self.cards][0:20]))

	def drawTopCard(self) :
		if len(self.cards) == 0 :
			raise GameOverException("No more cards")
		return self.cards.pop()


