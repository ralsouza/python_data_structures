from array import *

arr1 = array("i", [1,2,3,4,5,6])

def search_array(array, value): 
    for i in array: # --------------------------------------> O(n)
        if i == value:# ------------------------------------> O(1)
            return array.index(value) # --------------------> O(1)
    return "The element does not exist in this array." # ---> O(1)

print(search_array(arr1,3))
print(search_array(arr1,6))
print(search_array(arr1,7))