import json

def getDatabase():
    recipes = dict()
    with open('train.json') as data_file:
        data = json.load(data_file)
        for i in data:
            recipes[str(i["id"])] = i["ingredients"]
    return recipes;

#print(getDatabase())
