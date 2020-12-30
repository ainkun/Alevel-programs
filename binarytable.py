class binarytable:
    def __init__(self, data):
        self.LeftPointer = None
        self.RightPointer = None
        self.data = data

table=[]
pointer = 0

def insert(data):
    table.append(binarytable(data))
    n = len(table)

    def point(pointer):
        if n > 1:
            if data > table[pointer].data:
                if table[pointer].RightPointer == None:
                    table[pointer].RightPointer = n-1
                elif table[pointer].RightPointer != None:
                    pointer = table[pointer].RightPointer
                    point(pointer)
            
            if data < table[pointer].data:
                if table[pointer].LeftPointer == None:
                    table[pointer].LeftPointer = n-1
                elif table[pointer].LeftPointer != None:
                    pointer = table[pointer].LeftPointer
                    point(pointer)
    
    point(pointer)

list = ["hussain", "ali", "azan", "saqalain"]
for i in list:
    insert(i)


def printtable():
    for i in range(len(table)):
        print(str(table[i].RightPointer)+"   "+str(table[i].data+"   "+str(table[i].LeftPointer)))

printtable()


