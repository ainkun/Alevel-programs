data = [2,5,8,14,18,23]


def search(query,start,end):
    if int((start+end)%2) == 1:
        mid = int((start+end+1)/2)
        if query == data[mid]:
            return mid
        elif query > data[mid]:
            return search(query,mid,end)
        else:
            return search(query,start,mid-1)

    else:
        mid = int((start+end)/2)
        if query == data[mid]:
            return mid
        elif query > data[mid]:
            return search(query, mid+1, end)
        else:
            return search(query, start, mid-1)
    
    return mid
    

print(search(18,0,5))
