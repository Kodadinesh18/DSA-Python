# Brute Force Method for checking count between two arrays

# Array 'n' contains the main list of numbers
n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]

# Array 'm' contains the numbers we want to check frequencies for (in array 'n')
m = [10, 111, 1, 9, 67, 2]

# Dictionary to store number -> count mapping
hash_map = {}

# For every number in 'm', count how many times it appears in 'n'
for num in m:
    count = 0  # counter for each number
    for x in n:  # check each element in 'n'
        if num == x:  # if match found
            count += 1
    hash_map[num] = count  # store the final count in dictionary

# Print the frequency results
print(hash_map)
