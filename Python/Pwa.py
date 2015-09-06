import sys
from random import shuffle
from random import uniform


class Pwa(object):
	exp = []
	algWeight = 1.0
	name = 'PWA'

	def __init__(self):
		exp = []

	def add(self, e):
		self.exp.append(e)

	def getName(self):
		return self.name

	def getWeight(self):
		return self.algWeight

	def setWeight(self, _weight):
		self.algWeight = _weight

	def shuffle(self):
		shuffle(self.exp)

	def weightedChoice(self):
		maxf = 0.0
		minf = sys.float_info.min
		for e in self.exp:
			if (e.weight > maxf):
				maxf = e.weight
			if (e.weight < minf):
				minf = e.weight
		total = 0
		for e in self.exp:
			total = total + e.getWeight()
		r = uniform((minf/(2*total)),(maxf/total))
		for e in self.exp:
			if (e.weight/total >= r):
				return e
		raise Exception("Something Broke in Weighted Alg")


	def fixCosts(self, costs):
		for e in self.exp:
			for c in costs:
				if e.ticker == c.ticker:
					e.cost = c.cost
					break
		for e in self.exp:
			e.changeWeight(0.05)

	def toString(self):
		for e in self.exp:
			e.printExp()






