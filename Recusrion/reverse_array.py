#for reversing it is easier when we take arr,left,right

arr=[1,2,3,4,5,5,6,7,8,9]

def reverse_array(arr,left,right):
    if(left>=right):
        return
    arr[left],arr[right]=arr[right],arr[left]
    reverse_array(arr,left+1,right-1)
    return arr
print(reverse_array(arr,0,8))

#output:[8, 7, 6, 5, 5, 4, 3, 2, 1, 9]
