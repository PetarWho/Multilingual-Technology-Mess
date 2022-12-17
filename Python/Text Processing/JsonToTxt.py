import json

with open('colors.json') as json_file:
    colors = json.load(json_file)
    with open('colors.txt', 'w') as f:
        for color in colors.keys():
            f.write(color+"\n")
