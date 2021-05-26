print("My list:")
my_list = ["a","b","c","d","e","f"]
print(my_list)

# Slice operator [:]

print("\nSlice first two elements:")
# Second index is excluded
print(my_list[0:2])


print("\nSlice from the first index:")
print(my_list[1:])

print("\nUpdating first two elements:")
my_list[0:2] = ["x","y"]
print(my_list)

# List methods deletion: pop(), delete() and remove()
# pop() method
print("\nRemoving the 2nd element passing index position:")
my_list.pop(1)
print(my_list)

print("\nRemoving the last element passing without arguments:")
my_list.pop()
print(my_list)

print("\nPrinting the removed element:")
print(f"Excluded element '{my_list.pop(1)}'.")

# delete() method
my_list = ["a","b","c","d","e","f"]

print("\nDeleting element by index position:")
del my_list[2]
print(my_list)

print("\nDeleting element by index position:")
del my_list[2]
print(my_list)

print("\nDeleting many elements by slicing position:")
del my_list[:2]
print(my_list)

# remove() method
print("\nRemoving by elements itself:")
my_list.remove("e")
print(my_list)