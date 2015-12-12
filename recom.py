import json

userData = 'userData.txt'
movie = 'OMDb2.txt'
	
def storeJSON(name,year, opinion):
    f = open('userData.txt', 'a')
    f.write(str(name) + "(" + str(year) + ")|" + str(opinion))
	
def getMovie():
    print("hello")

def giveJSON(line):
    n= line
    i = 1
    with open("OMDb2.txt") as f:
        for line in f:
            if (n==i):
                return line
            else:
                i+=1

