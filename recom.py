import json

userData = 'userData.txt'
movie = 'OMDb2.txt'
	
def storeJSON(name,year, opinion):
    f = open('userData.txt', 'a')
    f.write(str(name) + " (" + str(year) + ")|" + str(opinion) + "\n")
	
def getMovie():
    dicti = [[23,0.8],[80,0.8],[70,0.8],[60,0.8],[50,0.8],[40,0.8],[30,0.8],]
    for mov in dicti:
        n= mov[0]
        i = 1
        with open("OMDbtransferable.txt") as f:
            for line in f:
                if (n==i):
                    return line
                else:
                    i+=1


def giveJSON(line):
    n= line
    i = 1
    with open("OMDb2.txt") as f:
        for line in f:
            if (n==i):
                return line
            else:
                i+=1

