from action import Action

class PlayCardAction(Action):
	def __init__(self, card) :
		self.card = card

	def getCard(self) :
		# print("Playing card {}".format(self.card))
		return self.card