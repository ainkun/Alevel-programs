height = []
maxsize = 5
for i in range(5):
    height.append(int(input()))

swapped = True
while swapped == True:
    swapped = False

    for i in range(maxsize-1):
        if height[i]>height[i+1]:
            height[i],height[i+1]=height[i+1],height[i]
            swapped = True
    maxsize=maxsize-1

for i in range(5):
    print(height[i])
