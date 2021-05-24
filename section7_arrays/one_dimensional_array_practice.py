from array import *

# 1. Create an array and transverse.

my_array = array("i",[1,2,3,4,5])

for i in my_array:
    print(i)


# 2. Access individual elements through indexes.
print("\nStep 2")

print(my_array[3])


# 3. Append any value to the array using append() method.
print("\nStep 3")

my_array.append(6)
print(my_array)


# 4. Insert value in an array using insert() method.
print("\nStep 4")

my_array.insert(3,11)
print(my_array)


# 5. Extend Python array using extend() method
print("\nStep 5")

my_array1 = array("i",[10,11,12])
my_array.extend(my_array1)
print(my_array)


# 6. Add items from list into array using fromlist() method
print("\nStep 6")

temp_list = [20,21,22]
my_array.fromlist(temp_list)
print(my_array)


# 7. Remove any array element using remove() method
print("\nStep 7")

# remove() removes the fist value found, when it's more than one
my_array.remove(11)
print(my_array)


# 8. Remove last array element using pop() method
print("\nStep 8")

my_array.pop()
print(my_array)

# 9. Fetch any element through it's index using index() method
print("\nStep 9")

print(my_array.index(21))

# 10. Reverse a Python array using reverse() method
print("\nStep 10")

my_array.reverse()
print(my_array)

# 11. Get array buffer information through buffer_info() method
print("\nStep 11")

print(my_array.buffer_info())
# The return is: (start from in memory, it has n elements)

# 12. Check for number of occurrences of an element using count() method
print("\nStep 12")

my_array.append(11)
print(my_array.count(11))
print(my_array)

# 13. Convert array to string using tostring() method
print("\nStep 13")

str_temp = my_array.tobytes()
print(str_temp)
ints = array("i")
ints.fromstring(str_temp)
print(ints)

# 14.  Convert array to a Python list with same elements using tolist() method
print("\nStep 14")

print(my_array.tolist())

# 15. Slice elements frmo an array
print("\nStep 15")

# 1st to 3th index, excluding the 4th
print(my_array[1:4])

# Starting from 2nd index
print(my_array[2:])

# Slice till the 4th index
print(my_array[:4])

# Slice all indexes
print(my_array[:])




