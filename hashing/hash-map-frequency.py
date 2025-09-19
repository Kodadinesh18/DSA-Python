#frequency count using dictionary or hash map in 2 different ways:
#for eg:we have an array and we need to count their frequency and store them in hashmap/dict
#method-1:

numbers = [5, 12, 7, 5, 18, 12, 7, 20, 25, 5, 18, 30, 12, 25, 7, 5, 40]
frequency_map={}

for i in range(0,len(numbers)):
    if numbers[i] in frequency_map:
        frequency_map[numbers[i]]+=1
    else:
        frequency_map[numbers[i]]=1

print(frequency_map)
#{5: 4, 12: 3, 7: 3, 18: 2, 20: 1, 25: 2, 30: 1, 40: 1}

#method2:using get in dictionary-
nums = [23, 45, 12, 23, 67, 45, 23, 89, 12, 45, 90, 67, 23, 12]
hash_map={}
for i in range(0,len(nums)):
    hash_map[nums[i]]=hash_map.get(nums[i],0)+1

print(hash_map)
#{23: 4, 45: 3, 12: 3, 67: 2, 89: 1, 90: 1}