from deck import Deck
from colour import Colour
from discard import Discard
from game_over_exception import GameOverException, CheatRulesException

class Table(object):
	def __init__(self):
		self.deck = Deck()
		self.tokens = 8
		self.fuse = 3

	def getTopCardFromDeck(self) :
		return self.deck.drawTopCard()

	def getTokens(self) :
		return self.tokens

	def addToken(self) :
		if self.tokens >= 8 :
			raise CheatRulesException("Already on have max tokens")
		self.tokens = self.tokens + 1

	def removeToken(self) :
		if self.tokens == 0 :
			raise CheatRulesException("No tokens to remove")
		self.tokens = self.tokens - 1

	def removeFuse(self) :
		self.fuse = self.fuse - 1
		if self.fuse == 0 :
			raise GameOverException("BOOM")


	def getFuse(self) :
		return self.fuse