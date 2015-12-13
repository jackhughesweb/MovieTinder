# recommender based on content + reviews

def makeCritset(number, shuffle = False):
    import sqlite3
    import random
    conn = sqlite3.connect('topcrits.db')
    #conn = sqlite3.connect('topcrits.db')
    c = conn.cursor()
    conn.text_factory = str
    
    critics = []
    for row in c.execute("select critID, count(*)  from reviews group by critID order by count(*) desc"):
        critics.append( (row[0],row[1]) )
    
    critset = []
    for critic in critics: critset.append(critic[0])
    if shuffle: random.shuffle(critset)
    return critset[:number]
    
def makeFilmset(number):
    import sqlite3
    conn = sqlite3.connect('topcrits.db')
    #conn = sqlite3.connect('topcrits.db')
    c = conn.cursor()
    conn.text_factory = str
    
    films = []
    for row in c.execute("select film, count(*)  from reviews group by film order by count(*) desc"):
        films.append((row[0],row[1]))

    filmset = []
    for film in films: filmset.append(film[0])
    return filmset[:number]
    
def makeConstrainedFilmset():
    import pickle
    RT_to_imdb = pickle.load( open( "RT_to_imdb.p", "rb" ) )
    
    films = []
    for key in RT_to_imdb:
        films.append(key)
    return films


def makeFeatureset(filmset,critset):
    import sqlite3
    conn = sqlite3.connect('topcrits.db')
    #conn = sqlite3.connect('topcrits.db')
    c = conn.cursor()
    conn.text_factory = str
    #print 'making featureset ...'
    
    # make film batches to query
    batchsize = 1000
    filmbatch = []
    batch = []
    for i,film in enumerate(filmset):
        if i % batchsize != batchsize-1:
            batch.append(film)
        else:
            filmbatch.append(batch)
            batch = []
    

    featureset = []
    for i,batch in enumerate(filmbatch):
        query = "SELECT * FROM reviews WHERE film IN ({seq}) ORDER BY film".format(seq=','.join(['?']*len(batch)))
        lastfilm = 0
        for row in c.execute(query, batch):
            crit = row[0]
            if crit not in critset: continue
            film = row[1]
            review = row[2].replace('\n','')
            if lastfilm == 0: 
                lastfilm = film
                dic = {}
            if film == lastfilm:
                dic[crit] = review
            else:
                dic['title'] = lastfilm
                featureset.append(dic)
                lastfilm = film
                dic = {}
    
    return featureset

def parseUserData():
    import pickle
    f = open('userData.txt', 'r')
    data = f.readlines()
    
    imdb_to_RT = pickle.load( open( "imdb_to_RT.p", "rb" ) )
    
    userReviews = {}
    for line in data:
        line = line.split('|')
        userReviews[imdb_to_RT[ line[0] ][0]] = line[1].replace('\n','')
        
    return userReviews
    
    
def labeledsetFromFeatureset(userReviews, featureset):
    labeledset = []
    for film in featureset:
        if film['title'] in userReviews:
            if userReviews[film['title']] == 'like':
                labeledset.append( (film, 'fresh') )
            elif userReviews[film['title']] == 'dislike':
                labeledset.append( (film, 'rotten') )
    return labeledset


def suggestions(labeledset, featureset, num = 20):
    from nltk import SklearnClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.svm import SVC, LinearSVC
    from sklearn.naive_bayes import MultinomialNB
    
    clf = SklearnClassifier(LogisticRegression(C=0.024))
    clf.train(labeledset)
    
    filmsSeen = []
    for film in labeledset:
        filmsSeen.append( film[0]['title'] )
    
    suggestions = []
    for film in featureset:
        if film['title'] in filmsSeen: continue
        suggestions.append( (film['title'], clf.prob_classify(film).prob('fresh') ))
        
    suggestions.sort(key=lambda x: x[1], reverse=True)
    return suggestions[:num]

def returnSuggestions(suggestions):
    import pickle
    returnList = []
    RT_to_imdb = pickle.load( open( "RT_to_imdb.p", "rb" ) )
    for line in suggestions:
        returnList.append( [RT_to_imdb[line[0]][1], round(line[1],3)] )
    return returnList
        
        
def suggestMovie(numSuggest = 20):
    critset = makeCritset(2000)
    filmset = makeConstrainedFilmset()
    featureset = makeFeatureset(critset, filmset)
    
    userReviews = parseUserData()
    featureset = makeFeatureset(filmset,critset)
    labeledset = labeledsetFromFeatureset(userReviews, featureset)
    suggests = suggestions(labeledset, featureset, numSuggest)
    suggests = returnSuggestions(suggests)
    return suggests

def makeLabeledset(testSubject,filmset,critset):
    import sqlite3
    conn = sqlite3.connect('topcrits.db')
    #conn = sqlite3.connect('topcrits.db')
    c = conn.cursor()
    conn.text_factory = str
    #print 'making featureset ...'
    
    # make film batches to query
    batchsize = 1000
    filmbatch = []
    batch = []
    for i,film in enumerate(filmset):
        if i % batchsize != batchsize-1:
            batch.append(film)
        else:
            filmbatch.append(batch)
            batch = []
    

    featureset = []
    for i,batch in enumerate(filmbatch):
        query = "SELECT * FROM reviews WHERE film IN ({seq}) ORDER BY film".format(seq=','.join(['?']*len(batch)))
        lastfilm = 0
        for row in c.execute(query, batch):
            crit = row[0]
            if crit == testSubject: continue
            if crit not in critset: continue
            film = row[1]
            review = row[2].replace('\n','')
            if lastfilm == 0: 
                lastfilm = film
                dic = {}
            if film == lastfilm:
                dic[crit] = review
            else:
                dic['title'] = lastfilm
                featureset.append(dic)
                lastfilm = film
                dic = {}
    
    # get likes and dislikes
    filmsLiked = []
    filmsDisliked = []
    for row in c.execute("SELECT * FROM reviews WHERE critID = ?", [testSubject]):
        if row[1] in filmset:
            if row[2] == 'fresh\n':
                filmsLiked.append(row[1])
            elif row[2] == 'rotten\n':
                filmsDisliked.append(row[1])
    
    labeledset = []
    for i,featureitem in enumerate(featureset):
        if featureitem['title'] in filmsLiked:
            labeledset.append( (featureitem, 'fresh') )
            continue
        if featureitem['title'] in filmsDisliked:
            labeledset.append( (featureitem, 'rotten') )
    return labeledset
    
    
def testClient(labeledset, fracLearn=0.8, LearnRate = 0.027, printing = True, SVM = False):
    import random
    from nltk import SklearnClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.svm import SVC, LinearSVC
    from sklearn.naive_bayes import MultinomialNB
    
    random.shuffle(labeledset)
    length = len(labeledset)
    trainset = labeledset[:int(length*fracLearn)]
    testset = labeledset[int(length*fracLearn):]
    
    if SVM:
        clf = SklearnClassifier(LinearSVC(C=LearnRate)) #LR C=0.0012, C=LinearSVC 0.0007
    else:
        clf = SklearnClassifier(LogisticRegression(C=LearnRate))
    clf.train(trainset)
    
    correct = 0
    for i,film in enumerate(testset):
        if clf.classify(film[0]) == film[1]:
            correct += 1
    testAcc = correct/float(len(testset))
    if printing: print 'Accuracy on test set: '+str(testAcc)
    correct = 0
    for i,film in enumerate(trainset):
        if clf.classify(film[0]) == film[1]:
            correct += 1
    trainAcc = correct/float(len(trainset))
    if printing: print 'Accuracy on train set: '+str(trainAcc)
    if not printing: return testAcc

def gridSearchC(start, end, labeledset, iters=10):
    ''' Start and en will be divided by 1,000 .'''
    x = []
    y = []
    for rate in range(start,end):
        C = float(rate)/1000
        score = 0
        print rate
        for i in range(iters):
            score += testClient(labeledset, LearnRate = C, printing = False)
        score = score /iters
        x.append(C)
        y.append(score)
    
    import matplotlib.pyplot as plt
    plt.scatter(x,y)
    plt.show()

def multitest(labeledset, iters, fracLearn=0.8, LearnRate = 0.027, printing=False, SVM = False):
    score = 0
    for i in range(iters):
        score += testClient(labeledset, fracLearn, LearnRate, False, SVM)
    if printing: print float(score)/iters
    else: return float(score)/iters

def simpleRT(labeledset, printing = True):
    correct = 0
    for i,film in enumerate(labeledset):
        likes = 0
        total = 0
        for key in film[0]:
            if film[0][key] not in ['fresh','rotten']: continue
            total += 1
            if film[0][key] == 'fresh':
                likes += 1
        if likes > total/2: p = 'fresh'
        else: p = 'rotten'
        if film[1] == p:
            correct += 1
    if printing: print 'Simple RT: '+str(correct/float(len(labeledset)))
    else: return correct/float(len(labeledset))

def nearCrits(crit, critset, filmset, fracTrain = 0.7, learnRate = 0.024):
    import random
    from nltk import SklearnClassifier
    from sklearn.linear_model import LogisticRegression
    
    labeledset = makeLabeledset(crit,filmset,critset)
    random.shuffle(labeledset)
    trainset = labeledset[:int(len(labeledset)*fracTrain)]
    
    clf = SklearnClassifier(LogisticRegression(C=learnRate))
    clf.train(trainset)
    
    critdist = []
    baseline = clf.prob_classify({}).prob('fresh')
    for crit in critset:
        quickdic = {}
        quickdic[crit] = 'fresh'
        dist = clf.prob_classify(quickdic).prob('fresh') - baseline
        critdist.append( (crit,dist) )
    critdist.sort(key=lambda x: x[1], reverse=True)
    for i in range(-10,10):
        print critdist[i]
