from database import *
from collections import defaultdict
#recipes - name of database

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

    print(ingreCount)
    return;


main()
