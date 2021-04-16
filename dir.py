from os import walk

b = list(walk("./static/"))[0][2]
print(b)