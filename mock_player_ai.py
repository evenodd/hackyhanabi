from give_information_action import GiveInformationAction
from colour_information import ColourInformation
from discard_card_action import DiscardCardAction

class MockPlayerAi(object) :

	def decideOnAction(self, id, hand, otherPlayers, discard, stacks, tokens) :
		# if tokens > 1 :
		# 	if id == 3 :
		# 		target = 0
		# 	else :
		# 		target = id + 1
		# 	player = list(filter(lambda p : p.getId() == target, otherPlayers))[0]
		# 	return GiveInformationAction(target, ColourInformation(
		# 		player.getCards()[0].getColour()
		# 	))

		# return DiscardCardAction(0)

		inputs = []

		# One input for the current player
		inputs.append(id)

		# One input for the colour and number of each card in your hand
		for card in hand :
			inputs.append(card.getNumber())
			colour = card.getColour()
			if colour != 0 :
				colour = colour.value
			inputs.append(colour)
		
		# One input for the colour and number of each card in every other player's hand
		for player in otherPlayers :
			for card in player.getCards() :
				inputs.append(card.getNumber())
				colour = card.getColour()
				if colour != 0 :
					colour = colour.value
				inputs.append(colour)

		# an input for the number of tokens
		inputs.append(tokens)

		# 5 inputs for each colour stack
		for stack in stacks.values() :
			inputs.append(stack)

		# 25 inputs for a count of each unique card in the discard pile 
		for colour in Colour.__members__.items() :
			for i in range(1, 5) :
				inputs.append(len(discard.getCards(colour, i)))

		

