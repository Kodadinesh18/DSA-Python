import array as arr

newarr=arr.array('i',[1,2,3,4,6,7,8])
n=len(newarr)

def linearsearch(arr,n,value):
    for i in range(0,n):
        if arr[i]==value:
            return i
    return -1
    
result=linearsearch(newarr,n,7)

if result==-1:
    print("item not found")
else:
    print("item found at index value:{}".format(result))