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
        
    
def main():
    ingredient = input('Enter an ingredient: ')
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
                        
    #print(ingreCount)
    print(getTopTwo(ingreCount))
    #getTopTwo(ingreCount)
    #ingreSort(ingreCount)
    return;


main()
