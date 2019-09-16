from pybrain.rl.environments import EpisodicTask 

class GameTask(EpisodicTask) :
	outdim = 103

	indim = 1

	numActions = 40

	# def performAction(self, action) :
	# 	print(action)
	# 	raise Exception()

	def isFinished(self) :
		return self.env.gameOver() or self.samples > 1000
		
	def getReward(self) :
		return self.env.getReward()