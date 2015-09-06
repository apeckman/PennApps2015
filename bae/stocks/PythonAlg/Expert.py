class Expert(object):
	ticker = None;
	cost = 0;
	weight = 0;

	def __init__(self, _ticker, _cost, _weight):
		self.ticker = _ticker
		self.cost = _cost
		self.weight = _weight

	def changeWeight(self, e):
		self.weight = self.weight * (1- (e * self.cost))

	def getWeight(self):
		return self.weight

	def toString(self):
		return self.ticker + ', ' + str(self.weight) + ', ' + str(self.cost)
