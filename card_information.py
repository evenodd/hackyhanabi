from card import Card

class CardInformation(object) :
	def __init__(self, card) :
		self.card = card
		self.number = 0
		self.colour = 0

	def getRealNumber(self) :
		return self.card.getNumber()

	def exposeNumber(self, number) :
		if self.getRealNumber() == number :
			self.number = number

	def getRealColour(self) :
		return self.card.getColour()

	def exposeColour(self, colour) :
		if self.getRealColour() == colour :
			self.colour = colour

	def getNumber(self) :
		return self.number

	def getColour(self) :
		return self.number

	def getCard(self) :
		return self.card

	def getInformationValue(self) :
		val = 0
		if self.number != 0 :
			val += 1
		if self.colour != 0 :
			val += 1
		return val

	def __str__(self) :
		return "{}{}".format(self.number, str(self.colour)[0])