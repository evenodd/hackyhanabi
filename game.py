from table import Table
from player import Player
from colour import Colour
from discard import Discard
from give_information_action import GiveInformationAction
from discard_card_action import DiscardCardAction
from play_card_action import PlayCardAction
from game_over_exception import GameOverException, CheatRulesException
from game_state import GameState
from numpy import log

class Game(object):
	def __init__(self, nbPlayers):
		self.table = Table()
		self.players = []
		self.gameDone = False
		self.currPlayer = 0
		self.discard = Discard()
		self.stacks = {}		
		for name, member in Colour.__members__.items() :
			self.stacks[name] = 0

		
		for i in range(nbPlayers) :
			self.players.append(Player(i))	
			for j in range(5) :
				self.players[i].draw(self.table.getTopCardFromDeck())

	def performAction(self, action) :
		if isinstance(action, GiveInformationAction) :
			target = action.getTarget() + self.currPlayer + 1
			if target >= 4 :
				target -= 4
			if target == self.currPlayer :
				raise CheatRulesException("Cant give information to self")
		
			self.table.removeToken()
			try :
				self.players[target].receiveInformation(action.getInformation())
			except CheatRulesException as error:
				# Give token back if move was invalid
				self.table.addToken()
				raise error
		
		if isinstance(action, DiscardCardAction) :
			self.discardCardFromPlayer(self.currPlayer, action.getCard())
			try :
				self.players[self.currPlayer].draw(self.table.getTopCardFromDeck())
			except GameOverException as error :
				# print(error)
				self.gameDone = True

		if isinstance(action, PlayCardAction) :
			try :
				self.playCard(self.currPlayer, action.getCard())
			except GameOverException as error :
				# print(error)
				self.gameDone = True
			try :
				self.players[self.currPlayer].draw(self.table.getTopCardFromDeck())
			except GameOverException as error :
				# print(error)
				self.gameDone = True

		if sum(self.stacks.values()) == 25 :
			self.gameDone = True
		
		self.currPlayer += 1				
		if(self.currPlayer == 4) :
			self.currPlayer = 0
		# print(str(self))

	def getState(self) :
		return GameState(
			self.players[self.currPlayer].getId(),
			self.players[self.currPlayer].getHand(),
			self.getOtherHands(self.players[self.currPlayer].getId()), 
			self.discard, 
			self.stacks, 
			self.table.getTokens(),
			self.table.getFuse()
		);

	def getScore(self) :
		score = sum(self.stacks.values()) +  self.table.getFuse() 
		# print(score)
		return score

	def getOtherHands(self, id) :
		return list(filter(lambda p : p.getId() != id, self.players))

	def discardCardFromPlayer(self, currPlayer, card) :
		self.table.addToken()
		self.discard.addCard(self.players[currPlayer].removeCard(card))

	def playCard(self, currPlayer, card) :
		card = self.players[currPlayer].removeCard(card)
		if self.stacks[card.getColour()] == card.getNumber() - 1 :
			self.stacks[card.getColour()] +=  1
			if self.stacks[card.getColour()] == 5 :
				try :
					self.table.addToken()
				except  CheatRulesExceptionas as error :
					# Dont punish ai for this
					pass
		else :
			self.discard.addCard(card)
			self.table.removeFuse()

	def isGameDone(self) :
		if self.gameDone :
			print(str(self))
		return self.gameDone

	def end(self) :
		self.gameDone = True

	def informationTotal(self) :
		return sum([p.getInformationValue() for p in self.players])

	def __str__(self) :
		return "C:{}|I:{}|S:{}|F:{}T:{}|D:{}".format(
			str.join(",", [
				str.join("", [
					str(c) for c in p.getCards()
				]) for p in self.players
			]),
			str.join(",", [
				str.join("", [
					str(c) for c in p.getHand()
				]) for p in self.players
			]),
			str.join("", [str(self.stacks[name]) for name, member in Colour.__members__.items()]),
			self.table.getFuse(),
			self.table.getTokens(),
			str(self.discard)
		)
 