import json

userData = 'userData.txt'
movie = 'OMDb2.txt'
	
def storeJSON(movie_id, opinion):
    f = open('userData.txt', 'a')
    f.write(str(movie_id) + "|" + str(opinion) + "\n")
	
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

