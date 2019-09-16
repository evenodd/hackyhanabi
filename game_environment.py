from pybrain.rl.environments.environment import Environment
from game import Game
from give_information_action import GiveInformationAction
from colour_information import ColourInformation
from number_information import NumberInformation
from discard_card_action import DiscardCardAction
from play_card_action import PlayCardAction
from colour import Colour
from game_over_exception import CheatRulesException
from scipy import array
class GameEnvironment(Environment) :
	outdim = 103

	indim = 1

	numActions=40

	def __init__(self) :
		self.game = Game(4)
		self.reward = 0
		self.actionArr = []
		self.cheatCount = 0
		for i in range(5) :
			self.actionArr.append(DiscardCardAction(i))
			self.actionArr.append(PlayCardAction(i))
		for target in range (3) :
			for colour, member in Colour.__members__.items() :
				self.actionArr.append(GiveInformationAction(
					target, 
					ColourInformation(colour)
				))
			for i in range(1, 6) :
				self.actionArr.append(GiveInformationAction(
					target, 
					NumberInformation(i)
				))
	
	def getSensors(self) :
		return self.game.getState().toInputs()

	def performAction(self, actionNb) :
		action = self.actionArr[int(actionNb)]
		beforeScore = self.game.getScore()
		try :
			self.game.performAction(action)
			self.reward = self.game.getScore() - beforeScore
			self.cheatCount = 0
		except CheatRulesException as error :
			# print("{}   E:{}".format(str(self.game), error))
			self.reward = 0
			self.cheatCount += 1
			if (self.cheatCount > 50) :
				self.game.end()

	def gameOver(self) :
		return self.game.isGameDone()

	def reset(self) :
		self.game = Game(4)
		self.reward = 0

	def getReward(self) :
		return self.reward

	def getScore(self) :
		return self.game.getScore()

