UserNameArray = ["567843Kamran", "765345Ali", "234543shameer", "112343hussain", "345654saifullah", "665432Samad"]
maxsize = len(UserNameArray)
swapped = True
while swapped == True:
    swapped = False

    for count in range(maxsize-1):
        x1=UserNameArray[count][:6]
        x2=UserNameArray[count+1][:6]

        if x1>x2:
            UserNameArray[count],UserNameArray[count+1]=UserNameArray[count+1],UserNameArray[count]
            swapped = True
    maxsize=maxsize-1
for i in range(len(UserNameArray)):
    print(UserNameArray[i])
