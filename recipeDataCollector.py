import json

with open('full_format_recipes.json') as data_file:
    data = json.load(data_file)

    print(data[0]["ingredients"])

