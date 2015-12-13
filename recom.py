import json
import backendFunctions as back
	
def storeJSON(name,year, opinion):
    f = open('userData.txt', 'a')
    f.write(str(name) + " (" + str(year) + ")|" + str(opinion) + "\n")
	
def getMovie():
    dicti = [[25,0.76],[34,0.82],[78,0.83]]
    nl="["
    for mov in dicti:
        n= mov[0]
        i = 1
        with open("OMDbtransferable.txt") as f:
            for line in f:
                print(line[1])
                if (n==i):
                    nl += line[:-2] + ', "Ratio": "' + str(mov[1]) + '"}, '
                    break
                else:
                   i+=1
    
    return nl[:-2] + ']'


def giveJSON(line):
    n= line
    i = 1
    with open("OMDbtransferable.txt") as f:
        for line in f:
            if (n==i):
                return line
            else:
                i+=1

"""
print("hello")
    for mov in dicti:
        n= mov[0]
        print(n)
        i = 1
        with open("OMDbtransferable.txt") as f:
            for line in f:
                print(line[1])
                if (n==i):
                    nl += line.replace('}', ', "Ratio": "' + str(mov[1]) + '"}')
                    break
                else:
                   i+=1

"""