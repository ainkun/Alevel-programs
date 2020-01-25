import pprint
dataval=[[80,80,255,80,80,255,80,80],
        [80,80,255,80,80,255,80,80],
        [255,80,120,120,120,120,255,80],
        [255,80,255,255,255,255,80,80],
        [255,80,120,120,120,120,80,80]]

pprint.pprint(dataval)
print('\n\n')

for y in range(len(dataval)):
    for x in range(int(len(dataval[0])/2)):
        dataval[y][x],dataval[y][7-x]=dataval[y][7-x],dataval[y][x]

pprint.pprint(dataval)
