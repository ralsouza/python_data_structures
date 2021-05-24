from array import *

arr1 = array("i", [1,2,3,4,5,6])

# Remove by index position.
# Removing at the beginning.
# Time Complexity:  O(n)
# Space Complexity: O(1)
arr1.remove(1)
print(arr1)

# Removing at the end.
arr1.remove(6)
print(arr1)

# Removing in the middle.
arr1.remove(4)
print(arr1)