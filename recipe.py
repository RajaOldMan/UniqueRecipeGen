#from database import *
from recipeDataCollector import *
from collections import defaultdict
#recipes - name of database



def getTopTwo(ingreCount):
    topTwo = ingreSort(ingreCount)
                    
    #print(topTwo)
    if len(topTwo) == 0:
        return ["-","-"]
        
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
        
def getIngreCount(ingredient, recipes):
    ingreCount = {}
    ingreCount = defaultdict(lambda: 0, ingreCount)
    skipList = [ingredient, "salt", "all-purpose flour", "pepper"]
    
    for recipe, ingreList in recipes.items():
        #for ingre in enumerate(v):
        #if ingredient is in ingreList then traverse the ingreList 
        #and if the ingre != ingredient then add to ingreCount        
        if ingredient in ingreList:
            for ingre in ingreList:    
                #add ingre to map if not ingredient & increment counter
                    if ingre not in skipList:
                        ingreCount[ingre] += 1

    #print(getTopTwo(ingreCount))
    return ingreCount;

def getUniqueIngre(ingreCount, topIngre, sorted, toSkip):
    diff = dict()
    for i in range(len(sorted)):
        if sorted[i] not in toSkip: 
            if sorted[i] not in list(ingreCount.keys()) and topIngre[sorted[i]] > 2:
                return sorted[i];
            else:
                diff[sorted[i]] = topIngre[sorted[i]] - ingreCount[sorted[i]]

    #print(sortedToDict(ingreSort(diff), diff))
    return ingreSort(diff)[0];

def sortedToDict(sorted, ingreCount):
    sortedDict = dict()
    for i in range(len(sorted)):
        sortedDict[sorted[i]] = ingreCount[sorted[i]]
    return sortedDict;

def main():
    recipes = getDatabase()
    ingredient = input('Enter an ingredient: ').lower()
    
    ingreCount = getIngreCount(ingredient,recipes)
    topTwo = getTopTwo(ingreCount)
    if topTwo[0] == "-":
        print("Ingredient does not exist")
        return;
    topIngre1 = getIngreCount(topTwo[0], recipes)
    topIngre2 = getIngreCount(topTwo[1], recipes)
    sorted1 = ingreSort(topIngre1)
    sorted2 = ingreSort(topIngre2)
    toSkip = [ingredient, topTwo[0], topTwo[1]]
    #print(getUniqueIngre(ingreCount, topIngre1, sorted1, toSkip))
    toSkip.append(getUniqueIngre(ingreCount, topIngre1, sorted1, toSkip))
    #print(getUniqueIngre(ingreCount, topIngre2, sorted2, toSkip))
    #print(sortedToDict(ingreSort(ingreCount), ingreCount))
    #print(sortedToDict(sorted1, topIngre1))
    #print(sortedToDict(sorted2, topIngre2))

    toSkip.append(getUniqueIngre(ingreCount, topIngre2, sorted2, toSkip))
    #print(ingreCount)
    #print(getTopTwo(ingreCount))
    #getTopTwo(ingreCount)
    #ingreSort(ingreCount)
    print(toSkip)
    
    return;


main()
