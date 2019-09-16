import struct
from colour import Colour 

class Card(object) :
	def __init__(self, colour : Colour, number):
		self.colour = colour
		self.number = number

	def __str__(self) :
		return "{}{}".format(self.number, self.colour[0])

	def getNumber(self) :
		return self.number

	def getColour(self) :
		return self.colour