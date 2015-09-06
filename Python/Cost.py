class Cost(object):
	ticker = None
	cost = None

	def __init__(self, _ticker, _cost):
		self.ticker = _ticker
		self.cost = _cost

	def toString(self):
		print str(ticker) + ', ' + str(cost)

