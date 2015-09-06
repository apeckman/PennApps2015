from AlgWeights import AlgWeights
from Pwa import Pwa
from Ftl import Ftl
from Expert import Expert
from Cost import Cost
#import mysql.connector
#import datetime

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

def readData(symbol, cost):
    ex = Expert(symbol, cost, 1.0)
    pactions.add(ex)
    factions.add(ex)

def writeFiles(filename):
    f = open(filename, 'w+')
    pw = pactions.weightedChoice()
    ft = factions.ftl()
    for e in pactions.exp:
        f.write(e.toString())
        f.write('\n')
    f.write("PWA: " + pw.toString() + '\n')
    f.write("FTL: " + ft.toString() + '\n')
    the_alg = algs.algChoice(2)
    f.write("AlgChooser: " + str(the_alg) + ", Weights: " +
        str(algs.pwa.getWeight()) + ", " + str(algs.ftl.getWeight()))
    algs.changeWeights(pw,ft)
    f.close()
    for e in pactions.exp:
        e.changeWeight(0.05)
    if the_alg == 'PWA':
        return (pw.toString())
    else:
        return (ft.toString())

def serializeData():
    f = open('stocks/PythonAlg/pickle_file.txt', 'wb')
    f.write(pactions.getName() + ' ' + str(pactions.getWeight()) + ' ')
    f.write(factions.getName() + ' ' + str(factions.getWeight()) + '\n')
    for e in pactions.exp:
        f.write(e.toString())
        f.write('\n')
    f.close()

def deserializeData():
    f = open('stocks/PythonAlg/pickle_file.txt', 'rb')
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

def updateCosts(ticker, cost):
    for e in pactions.exp:
        if ticker == e.ticker:
            e.setCost(cost)
            break

def main():
    filename = "stocks/PythonAlg/experts.txt"
    """
    cnx = mysql.connector.connect(user='frias',password='D1lp1226',database='stocks')
    cursor = cnx.cursor()

    a_query = "SELECT symbol, open_p, close_p from price group by symbol order by date_ex desc"
    cursor.execute(a_query)
    for (symbol, open_p, close_p) in cursor:
        readData(str(symbol),(open_p/close_p)-1)

    i_query = "SELECT date_ex from price where YEAR(date_ex) >= '2010' group by date_ex"
    cursor.execute(i_query)
    date_list = cursor.fetchall()

    f_query = "SELECT symbol, open_p, close_p from price where date_ex = %s"
    for d in date_list:
        print "in date"
        cursor.execute(f_query, d)
        for (symbol, open_p, close_p) in cursor:
            if close_p == 0:
                updateCosts(str(symbol), float(0.0))
                continue
            updateCosts(str(symbol), float((open_p/close_p)-1))
        pactions.shuffle()
        pw = pactions.weightedChoice()
        ft = factions.ftl()
        algs.algChoice()
        algs.changeWeights(pw,ft)
        for e in pactions.exp:
            e.changeWeight(0.05)

    cursor.close()
    cnx.close()
    """
    deserializeData()
    pactions.shuffle()
    temp = writeFiles(filename)
    temp_1 = writeFiles(filename)
    temp_2 = writeFiles(filename)
    temp_3 = writeFiles(filename)
    temp_4 = writeFiles(filename)
    serializeData()
    return (temp, temp_1, temp_2, temp_3, temp_4)

if __name__ == "stocks.PythonAlg.main":
    __name__ = main()





