from colour import Colour

class GameState(object) :
	def __init__(self, playerId, hand, otherPlayers, discard, stacks, tokens, fuse) :
		self.playerId = playerId
		self.hand = hand
		self.otherPlayers = otherPlayers
		self.discard = discard
		self.stacks = stacks
		self.tokens = tokens
		self.fuse = fuse

	def toInputs(self) :
		inputs =[]
		inputs.append(self.playerId)

		# One input for the colour and number of each card in your hand
		for card in self.hand :
			inputs.append(card.getNumber())
			colour = card.getColour()
			# if colour != 0 :
			# 	print(colour)
			# 	colour = Colour[colour].value
			inputs.append(colour)
		
		# One input for the colour and number of each card in every other player's hand
		for i in range(self.playerId + 1, self.playerId + 4) :
			if i >= 4 :
				i -= 4
			player = list(filter(
				lambda p : p.getId() == i, 
				self.otherPlayers
			))[0]

			for card in player.getHand() :
				inputs.append(card.getNumber())
				colour = card.getColour()
				# if colour != 0 :
				# 	print(colour)
				# 	colour = Colour[colour].value
				inputs.append(colour)


		# One input for the colour and number of each card in every other player's hand
		for i in range(self.playerId + 1, self.playerId + 4) :
			if i >= 4 :
				i -= 4
			player = list(filter(
				lambda p : p.getId() == i, 
				self.otherPlayers
			))[0]

			for card in player.getCards() :
				inputs.append(card.getNumber())
				colour = card.getColour()
				if colour != 0 :
					colour = Colour[colour].value
				inputs.append(colour)

		# an input for the number of tokens
		inputs.append(self.tokens)
		inputs.append(self.fuse)

		# 5 inputs for each colour stack
		for stack in self.stacks.values() :
			inputs.append(stack)

		# 25 inputs for a count of each unique card in the discard pile 
		for colour in Colour.__members__.items() :
			for i in range(1, 6) :
				inputs.append(len(self.discard.getCards(colour, i)))
		
		# print(len(inputs), inputs)
		return inputs