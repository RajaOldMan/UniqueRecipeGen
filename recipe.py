from database import *
from collections import defaultdict
#recipes - name of database

def getTopTwo(ingreCount):
    topTwo = ["", ""]
    for ingre, count in ingreCount.items():
        if topTwo[0] == "":
            topTwo[0] = ingre
        else:
            for i in range(len(topTwo)):
                if ingreCount[topTwo[i]] <= count:
                    if i == 0:
                        topTwo[1] = topTwo[0]
                        topTwo[0] = ingre
                        break;
                    else:
                        topTwo[1] = ingre
                elif ingreCount[topTwo[1]] == "":
                    topTwo[1] = ingre
                    break;
                    
    print(topTwo)    
    return;
    
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
    getTopTwo(ingreCount)
    return;


main()
