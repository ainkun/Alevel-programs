height = [45, 67, 23, 45, 21, 78, 90, 11, 21]
maxsize = len(height)-1
counter = 0

swapped = True
while swapped == True:
    swapped = False
    for count in range(maxsize):
        if height[count]>height[count+1]:
            height[count],height[count+1]=height[count+1],height[count]
            swapped = True
            pos=count
        counter=counter+1
    maxsize=pos

for i in range(len(height)):
    print(i+1,': ',height[i])

print('The algo analysis : ',counter)
    
