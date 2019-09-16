from action import Action

class DiscardCardAction(Action):
	def __init__(self, card) :
		self.card = card

	def getCard(self) :
		# print("Discarding card {}".format(self.card))
		return self.card