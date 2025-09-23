#1.selection sort:

nums=[4,3,2,8,5,7,1]
n=len(nums)

def selectionsort(arr):
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
            nums[i],nums[min_index]=nums[min_index],nums[i]


selectionsort(nums)
print(nums)

