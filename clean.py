"""
it is a program to generate a 'cleaned' file
in this case, a file with all '#' removed and all content on a new line.
'"""
f = open('word5Dict.txt' ,"r")
flines = f.read().splitlines()
fdata = []
for fline in flines:
    info = fline.split("#")
    fdata.append(info)

stuff = sum(fdata,[])
stuff.remove('')

g = open("scrabble5.txt", "w")
for x in range(len(stuff)):
    print(stuff[x], file=g)
g.close()
