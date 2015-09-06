from random import shuffle
from random import uniform

import Pwa
import Ftl
import Expert
import Cost

class AlgWeights(object):
	algs = []
	pwa = None
	ftl = None
	# The other Alg
	pastchoice = None

	def __init__(self, _pwa, _ftl):
		self.pwa = _pwa
		self.ftl = _ftl
		self.algs.append(self.pwa)
		self.algs.append(self.ftl)

	def algChoice(self):
		return chooser(randFloat((findMin()/(2*sumWeights())), (findMax()/sumWeights())));

	def findMax(self):
		return max(self.pwa.getWeight(),self.ftl.getWeight())

	def findMin(self):
		return min(self.pwa.getWeight(),self.ftl.getWeight())

	def sumWeights(self):
		return self.pwa.getWeight() + self.ftl.getWeight()

	def randFloat(self, _min, _max):
		return uniform(_min,_max)

	def chooser(self, r):
		shuffle(self.algs)
		for a in self.algs:
			if a.getWeight() >= r:
				self.pastchoice = a
				return a.getName()
		raise Exception("Messed up in AlgWeights")

	def algChoice(self):
		return self.chooser(self.randFloat(self.findMin()/(2*self.sumWeights()), self.findMax()/self.sumWeights()));

	def changeWeights(self, p, f):
		choice = None
		if self.pastchoice.getName() == 'PWA':
			choice = p;
		if self.pastchoice.getName() == 'FTL':
			choice = f;
		if choice.cost < 0.0:
			self.pastchoice.setWeight(self.pastchoice.getWeight() * 
				(1 - (0.05 * float(choice.cost))))
		elif choice.cost > 0.0:
			self.pastchoice.setWeight(self.pastchoice.getWeight() * 
				(1 + (0.05 * float(choice.cost))))	




