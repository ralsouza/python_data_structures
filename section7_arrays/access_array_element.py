from array import *

arr1 = array("i", [1,2,3,4,5,6])

def access_element(array, index):
    if index >= len(array):
        print("There is not any element in this index.")
    else:
        print(array[index])

access_element(arr1, 1)
access_element(arr1, 8)
access_element(arr1, 6)