import array as arr

list1=arr.array('i',[1,2,3,4,6,7,8])
n=7

def binarysearch(list1,n):
    low=0
    high=len(list1)-1
    mid=0
    while low <=high:
        mid=(low+high)//2
        
        if list1[mid]<n:
            low=mid+1
        elif list1[mid]>n:
            high=mid-1
        else:
            return mid 
    return -1
    
result=binarysearch(list1,n)

if result==-1:
    print("item not found")
else:
    print("item found at {}".format(result))