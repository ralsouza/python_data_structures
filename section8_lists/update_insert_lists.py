# Update/Insert - List

my_list = [1,2,3,4,5,6,7]
print(my_list)

# Updating 2nd and 4th position - Time Complexity: O(1)
print("\nUpdating list:")
my_list[2] = 33
my_list[4] = 55
print(my_list)

# 1. Inserting an element to the beginning of the list
print("\nInserting value 11 o the beginning:")

my_list.insert(0,11)
print(my_list)


# 2. Inserting and element to the any given place in the list
print("\nInserting value 15 at 4th position:")

my_list.insert(4, 15)
print(my_list)


# 3. Inserting an element to the end of the list
print("\nInserting an element to the end of the list:")

my_list.append(55)
print(my_list)


# 4. Inserting another list to the list
print("\nInserting another list to the list:")

new_list = [11,12,13,14]
my_list.extend(new_list)
print(my_list)