# Binary Search
# - Binary Search is faster than Linear Search;
# - Half of the remaining element can be eliminated at a time, 
#   instead of eliminating them on by one;
# - ** Binary Search only works for sorted arrays **

# Pseudocode
# - Create a function with two parameters which are a sorted array and value.
# - Create two pointers: a left pointer at the start of the array and a right 
#   pointer at the end of the array.
# - Based on left and right pointers calculate middle pointer.
# - While middle is not equal to the value and start <= end loop:
#   - If the middle is greater than the value move the right pointer down.
#   - If the middle is less than the value move the left pointer up.
# - If the value is never found return 1.

import math

def binary_search(array, value):
    start = 0
    end = len(array) - 1
    middle = math.floor((start + end)/2)

    while not(array[middle] == value) and start <= end:
        if value < array[middle]:
            end = middle - 1 # Move new middle index before the current middle
        else:
            start = middle + 1 # Move new middle index after the current middle
        middle = math.floor((start + end)/2) # Recalculate the middle index
        # print(start, middle, end) # Test pointers
    if array[middle] == value:
        return middle
    else:
        return -1

arr = [8,9,12,15,17,19,20,21,28]

print(binary_search(arr,15))

# [8,9,12,15,17,19,20,21,28]
#  S          M           E
#  S M     E
#      SM  E
#         SME

# Test nonexistent value
print(binary_search(arr,100))