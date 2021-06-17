# Linear Search
# 1. Create a function with two parameters which are an array and a value
# 2. Loop through the array and check if the current array element is equal to the value
# 3. If it is return the index at which the element is found
# 4. If the value is never found return -1

def linear_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1


arr = [20,40,30,50,90]
value = 100

print(linear_search(arr, value))