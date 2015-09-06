# in class PWA
def weightRank(self):
	weightList = []
	for expert in self.exp:
		weightList.append((expert.ticker, expert.getWeight()))
	return sorted(weightList, key = lambda expert: expert[1])

def costRank(self):
	costList = []
	for expert in self.exp:
		costList.append((expert.ticker, expert.getCost()))
	return sorted(weightList, key = lambda expert: expert[1])

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

	def algChoice(self,term):
		return chooser(randFloat((findMin()/(2*sumWeights())), (findMax(term)/sumWeights())),term);

	def findMax(self,term):
        if term == 1: # short
            return max(self.pwa.getWeight()*0.3,self.ftl.getWeight()*0.7)
        if term == 3: # long
            return max(self.pwa.getWeight()*0.7,self.ftl.getWeight()*0.3)
		return max(self.pwa.getWeight(),self.ftl.getWeight())

	def findMin(self):
		return min(self.pwa.getWeight(),self.ftl.getWeight())

	def sumWeights(self):
		return self.pwa.getWeight() + self.ftl.getWeight()

	def randFloat(self, _min, _max):
		return uniform(_min,_max)

	def chooser(self, r, term = 2):
		if term == 0: # very short
            self.pastchoice = ftl.getName()
			return self.ftl.getName()

        if term == 4: # very long
            self.pastchoice = pwa.getName()
            return self.pwa.getName()

        if term == 1: # short
            t_pwa = self.pwa.getWeight()*0.3
            t_ftl = self.ftl.getWeight()*0.7
            if t_pwa >= r:
               self.pastchoice = pwa.getName()
               return self.pwa.getName()
             else:
                self.pastchoice = ftl.getName()
                return self.ftl.getName()

        if term == 3: # long
            t_pwa = self.pwa.getWeight()*0.7
            t_ftl = self.ftl.getWeight()*0.3
            if t_ftl >= r:
                self.pastchoice = ftl.getName()
                return self.ftl.getName()
             else:
                self.pastchoice = pwa.getName()
                return self.pwa.getName()

        if term == 2: # neutral
		  shuffle(self.algs)
		  for a in self.algs:
			 if a.getWeight() >= r:
				    self.pastchoice = a
				    return a.getName()
		  raise Exception("Messed up in AlgWeights")
        else:  
            raise Exception("Please enter a valid term")

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


            