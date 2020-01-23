height = [45, 67, 23, 45, 21, 78, 90, 11, 21]
maxsize = len(height)
counter = 0

swapped = True
while swapped == True:
    swapped = False
    for count in range(maxsize-1):
        if height[count]>height[count+1]:
            height[count],height[count+1]=height[count+1],height[count]
            swapped = True
        counter=counter+1
    maxsize=maxsize-1

for i in range(9):
    print(i+1,': ',height[i])

print('The algo analysis : ',counter)
    