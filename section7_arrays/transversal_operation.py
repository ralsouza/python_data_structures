from array import *

arr1 = array("i", [1,2,3,4,5,6])

# arr1.insert(2,9)
# print(arr1)

def transverse_array(array):
    for i in array: # --------> O(n)
        print(i) # -----------> O(1)

transverse_array(arr1)