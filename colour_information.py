from colour import Colour

class ColourInformation(object) :
	def __init__(self, colour : Colour) :
		self.colour = colour

	def getInformation(self) :
		return self.colour