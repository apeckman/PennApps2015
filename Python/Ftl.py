import sys

class Ftl(object):
	exp = []
	algWeight = 1.0
	name = 'FTL'

	def __init__(self):
		self.exp = []

	def getName(self):
		return self.name

	def getWeight(self):
		return self.algWeight

	def setWeight(self,_weight):
		self.algWeight = _weight

	def add(self, e):
		self.exp.append(e)

	def ftl(self):
		name = None
		maxf = sys.float_info.max
		for e in self.exp:
			if (e.cost < maxf):
				name = e
				maxf = e.cost
		return name



