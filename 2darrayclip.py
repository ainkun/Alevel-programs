picture = [[240, 10, 10, 10, 10, 10, 10, 240],
           [80, 80, 240, 80, 80, 240, 80, 80],
           [80, 80, 240, 80, 80, 240, 80, 80],
           [80, 80, 150, 150, 150, 150, 80, 80],
           [80, 80, 240, 240, 240, 240, 80, 80],
           [80, 80, 150, 150, 150, 150, 80, 80],
           [240, 240, 150, 150, 150, 150, 240, 240],
           [240, 240, 150, 150, 150, 150, 240, 240]]

def clip(MaxVal):
    clipflag = False
    for y in range(len(picture)):
        for x in range(len(picture[0])):
            if  picture[y][x] > MaxVal:
                picture[y][x] = MaxVal
                clipflag = True
    return clipflag

