from collections import deque

class Expert(object):
	ticker = None
	cost = 0
	weight = 0

	def __init__(self, _ticker, _cost, _weight):
		self.ticker = _ticker
		self.cost = _cost
		self.weight = _weight

	def changeWeight(self, e):
		self.weight = self.weight * (1- (e * float(self.cost)))

	def getWeight(self):
		return self.weight

	def getCost(self):
		return self.cost

	def setCost(self,_cost):
		self.cost = _cost

	def toString(self):
		return self.ticker + ', ' + str(self.weight) + ', ' + str(self.cost)
