from card import Card

class Discard(object):
	def __init__(self):
		self.cards = []

	def getCard(self, i) :
		return self.cards[i]
	
	def getSize(self) :
		return len(self.cards)

	def addCard(self, card : Card) :
		self.cards.append(card)

	def getCards(self, colour, number) :
		return list(filter(
			lambda c : c.getNumber() == number and c.getColour() == colour, 
			self.cards
		))

	def __str__(self) :
		return str.join("",[str(c) for c in self.cards])
