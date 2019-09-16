from card import Card
from card_information import CardInformation
from number_information import NumberInformation
from colour_information import ColourInformation
from game_over_exception import CheatRulesException


class Player(object):
	def __init__(self, id) :
		self.id = id
		self.hand = []
	
	def getId(self) :
		return self.id	

	def draw(self, card : Card) :
		self.hand.append(CardInformation(card))

	def decideOnAction(self, othersHands, discard, stacks, tokens) :
		# return self.ai.decideOnAction(self.id, self.hand, othersHands, discard, stacks, tokens)
		pass
		
	def receiveInformation(self, information) :
		if isinstance(information, NumberInformation) :
			if any(information.getInformation() == handCard.getRealNumber() for handCard in self.hand) :
				for i in range(len(self.hand)) :
					self.hand[i].exposeNumber(information.getInformation())
			else :
				raise CheatRulesException("Cant give information about cards not in hand")

		if isinstance(information, ColourInformation) :
			if any(information.getInformation() == handCard.getRealColour() for handCard in self.hand) :
				for i in range(len(self.hand)) :
					self.hand[i].exposeColour(information.getInformation())
			else :
				raise CheatRulesException("Cant give information about cards not in hand")
				# 	"Cant give information {}, about cards not in hand: {}"
				# 	.format(information.getInformation(), list(map(
				# 		lambda c:str(c.getCard()), self.hand
				# 	)))
				# )

	def removeCard(self, card) :
		return self.hand.pop(card).getCard()

	def getHand(self) :
		return self.hand

	def getInformationValue(self) :
		return sum([c.getInformationValue() for c in self.hand])

	def getCards(self) :
		return list(map(lambda c:c.getCard(), self.hand) )



