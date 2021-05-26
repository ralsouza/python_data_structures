# Searching for an element in the list.
# IN operator
# Linear search

my_list = [10,20,30,40,50,60,70,80,90]
print(f"My list: {my_list}")

# IN operator
print("\nSearching a value by IN operator:")

value = 20

if value in my_list:
    print(f"- The index of {value} value is {my_list.index(value)}.")
else:
    print("- The value does not exist in the list.")

# Linear search
print("\nSearching a value by linear search:")

def searching_list(list, value):
    for i in list:
        if i == value:
            return f"- The index of {value} value is {my_list.index(value)}."
    return "- The value does not exist in the list."

value = 50
print(searching_list(my_list, value))

value = 100
print(searching_list(my_list, value))