StudentName=["salman", "kamran", "bashir", "zohaib", "mohsin", "ali", "####", "####", "####", "####"]
emparr = '####'
c=len(StudentName)
unused=0

for i in range(c):
    if StudentName[i]=='####':
        unused=unused+1
    else:
        StudentName[i]=StudentName[i][0].upper()+StudentName[i][1:]
maxsize=unused

swapped=False
while swapped == False:
    swapped=True
    for i in range(c-1-maxsize):
        if StudentName[i]>StudentName[i+1]:
            temp=StudentName[i]
            StudentName[i]=StudentName[i+1]
            StudentName[i+1]=temp
            swapped=False
    maxsize=maxsize+1

for i in range(c-unused):
    print(i+1, 'NAME: ', StudentName[i])
        
