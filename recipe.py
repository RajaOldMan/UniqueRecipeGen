from database import *
from collections import defaultdict
#recipes - name of database

def getTopTwo(ingreCount):
    topTwo = ingreSort(ingreCount)
                    
    #print(topTwo)    
    return [topTwo[0], topTwo[1]];

def ingreSort(ingreCount):
    sorted = list(ingreCount.keys())
    for i in range( len(sorted)):
        for k in range( len(sorted) - 1, i, -1):
            if ingreCount[sorted[k]] > ingreCount[sorted[k - 1]]:
                    swap(sorted, k, k - 1)
                
   #print(sorted)
    return sorted;

                
def swap(sorted, x, y):
    tmp = sorted[x]
    sorted[x] = sorted[y]
    sorted[y] = tmp
        
def getIngreCount(ingredient):
    ingreCount = {}
    ingreCount = defaultdict(lambda: 0, ingreCount)
    
    for recipe, ingreList in recipes.items():
        #for ingre in enumerate(v):
        #if ingredient is in ingreList then traverse the ingreList 
        #and if the ingre != ingredient then add to ingreCount        
        if ingredient in ingreList:
            for ingre in ingreList:    
                #add ingre to map if not ingredient & increment counter
                    if ingre != ingredient:
                        ingreCount[ingre] += 1

    #print(getTopTwo(ingreCount))
    return ingreCount;

def getUniqueIngre(ingreCount, topIngre, sorted, ingredient):
    diff = dict()
    for i in range(len(sorted)):
        if sorted[i] != ingredient: 
            if sorted[i] not in list(ingreCount.keys()) and topIngre[sorted[i]] > 2:
                return sorted[i];
            else:
                diff[sorted[i]] = topIngre[sorted[i]] - ingreCount[sorted[i]]

    return ingreSort(diff)[0];

def sortedToDict(sorted, ingreCount):
    sortedDict = dict()
    for i in range(len(sorted)):
        sortedDict[sorted[i]] = ingreCount[sorted[i]]
    return sortedDict;

def main():
    ingredient = input('Enter an ingredient: ')
    
    ingreCount = getIngreCount(ingredient)
    topTwo = getTopTwo(ingreCount)
    topIngre1 = getIngreCount(topTwo[0])
    topIngre2 = getIngreCount(topTwo[1])
    sorted1 = ingreSort(topIngre1)
    sorted2 = ingreSort(topIngre2)
    print(getUniqueIngre(ingreCount, topIngre1, sorted1, ingredient))
    print(getUniqueIngre(ingreCount, topIngre2, sorted2, ingredient))
    print(sortedToDict(ingreSort(ingreCount), ingreCount))
    print(sortedToDict(sorted1, topIngre1))
    print(sortedToDict(sorted2, topIngre2))
    
    #print(ingreCount)
    #print(getTopTwo(ingreCount))
    #getTopTwo(ingreCount)
    #ingreSort(ingreCount)
    
    return;


main()
