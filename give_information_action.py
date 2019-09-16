from action import Action

class GiveInformationAction(Action):
	def __init__(self, target, information) :
		self.target = target
		self.information = information


	def getTarget(self) :
		return self.target

	def getInformation(self) :
		# print("Giving information to player {} about information {}"
		# 	.format(self.target, self.information.getInformation()))
		return self.information