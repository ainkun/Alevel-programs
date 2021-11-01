#!/bin/python3

class BT:
    def __init__(self):
        self.LeftPointer = 0
        self.RightPointer = 0
        self.Data = ""

dsBT = []

for i in range(10):
    dsBT.append(BT())

def insertBT(val):
    currPos = 0
    tPos = 0
    while True:
        if dsBT[currPos].Data == "":
            dsBT[currPos].Data = val

        elif val > dsBT[currPos].Data:
            if dsBT[currPos].RightPointer == 0:
                tPos = currPos
                while dsBT[tPos].Data != "":
                    tPos = tPos + 1
                dsBT[tPos].Data = val
                dsBT[currPos].RightPointer = tPos
            else:
                currPos = dsBT[currPos].RightPointer
        
        else:
            if dsBT[currPos].LeftPointer == 0:
                tPos = currPos
                while dsBT[tPos].Data != "":
                    tPos = tPos + 1
                dsBT[tPos].Data = val
                dsBT[currPos].LeftPointer = tPos
            else:
                currPos = dsBT[currPos].LeftPointer


def main():
    for i in range(10):
        valBT = input("Enter Vidoe Game Name: ")
        insertBT(valBT)

    print(len(dsBT))

    for i in range(10):
        print(dsBT[i].Data)
        print(dsBT[i].LeftPointer)
        print(dsBT[i].RightPointer)

    print(dsBT)


main()
