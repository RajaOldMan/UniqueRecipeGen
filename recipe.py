from database import *
#recipes - name of database

def main():
    ingredient = input('Enter an ingredient: ')

    for k, v in recipes.items():
        #for ingre in enumerate(v):
        for ingre in v:    
            if ingre == "Spinach":
                print(ingre)

    return;

main()
