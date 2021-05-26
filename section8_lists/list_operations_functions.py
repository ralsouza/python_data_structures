# List operations / functions.

# + operator: concatenate lists
a = [1,2,3]
b = [4,5,6]
print(f"My lists: \na={a} \nb={b}")

print("\nConcatenated lists by + operador:")
c = a + b
print(c)

print("\n* operador:")
d = [0,1]
e = d * 4
print(f"a list was multiplied 4 times: {e}")

# len(): return count of elements in the list
print("\nCounting the elements:")
a = [0,1,2,3,4,5,6]
print(len(a))

# max(): returns the item with the highest value in the list
print("\nMax value in the list:")
print(max(a))

# min(): returns the item with the lowest value in the list
print("\nMin value in the list:")
print(min(a))

# sum(): returns the sum of all items in the list
print("\nSum value in the list:")
print(sum(a))

# Combining functions
# Computing the average of the list
print("\nAverage value of the list:")
print(sum(a)/len(a))

# ------- Mini Challenge --------
def compute_avg():
    list = []
    while (True):
        input_number = input("Enter a number: ")
        if input_number == "done":
            break
        else:
            list.append(float(input_number))
    return (sum(list)/len(list))
    
print(f"The average is: {compute_avg()}")