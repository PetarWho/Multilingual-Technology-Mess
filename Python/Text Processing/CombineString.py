prefix = "hover"
attribute = "color"
suffix = ":hover"
colorsFile = "colors.txt"
outputFile = "hover-colors.txt"

with open(colorsFile) as colors:
    with open(outputFile, 'w') as f:
        for color in colors:
            color = color[:-1]
            f.write(f"\n{prefix}-{color}{suffix}" + "{\n" + f"{attribute}: {color}" + "\n}\n")
