from array import *

# Array creation.
arr1 = array("i", [1,2,3,4,5])
print(arr1)

# Inserting a new element at the end.
# Time Complexity: O(1)
arr1.insert(6,7) # .index(index, element)
print(arr1)

# Inserting a new element at the beginning.
arr1.insert(0,0)
print(arr1)

# Inserting a new element in the middle.
# Time Complexity: O(n)
arr1.insert(1,9)
print(arr1)