from AlgWeights import AlgWeights
from Pwa import Pwa
from Ftl import Ftl
from Expert import Expert
from Cost import Cost

path = ""
line = ""
filename = ""
pactions = Pwa()
factions = Ftl()
algs = AlgWeights(pactions, factions)

def readFiles(path):
	ticker = ""
	_open = 0.0
	_close = 0.0
	ex = None
	f = open(path, 'r')
	for line in f:
		# might have to change
		l = line.split(',')
		ticker = l[0]
		_open = float(l[2])
		_close = float(l[5])
		ex = Expert(ticker, (_open/_close)-1, 1.0)
		pactions.add(ex)
		factions.add(ex)
	f.close()

def writeFiles(filename):
	f = open(filename, 'w+')
	pw = pactions.weightedChoice()
	ft = factions.ftl()
	for e in pactions.exp:
		f.write(e.toString())
		f.write('\n')
	f.write("PWA: " + pw.toString() + '\n')
	f.write("FTL: " + ft.toString() + '\n')
	f.write("AlgChooser: " + str(algs.algChoice()) + ", Weights: " +
		str(algs.pwa.getWeight()) + ", " + str(algs.ftl.getWeight()))
	algs.changeWeights(pw,ft)
	f.close()
	for e in pactions.exp:
		e.changeWeight(0.1)

def serializeData():
	f = open('pickle_file.txt', 'wb')
	f.write(pactions.getName() + ' ' + str(pactions.getWeight()) + ' ')
	f.write(factions.getName() + ' ' + str(factions.getWeight()) + '\n')
	for e in pactions.exp:
		f.write(e.toString())
		f.write('\n')
	f.close()

def deserializeData():
	f = open('pickle_file.txt', 'rb')
	alg = f.readline().split()
	pactions.setWeight(float(alg[1]))
	factions.setWeight(float(alg[3]))
	for line in f:
		l = line.split(',')
		ticker = l[0]
		weight = float(l[1])
		cost = float(l[2])
		ex = Expert(ticker, cost, weight)
		pactions.add(ex)
		factions.add(ex)
	f.close()

def main():
	deserializeData()
	path = "NYSE_20150623(1).csv"
	filename = "experts.txt"
	#readFiles(path)
	pactions.shuffle()
	writeFiles(filename)
	serializeData()

if __name__ == "__main__":
    main()


	