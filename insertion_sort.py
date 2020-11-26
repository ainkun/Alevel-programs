arr=[]
arr = [74,8,4,8,1,34,12,2]

for i in range(len(arr)):
    curr=arr[i]
    j=i-1

    while j>=0 and arr[j]>curr:
         arr[j+1]=arr[j]
         j=j-1
    arr[j+1]=curr

print(arr)

