# Duplicate Number
# Write a function to find the duplicate number on given integer array/list.
# Example: remove_duplicates([1,1,2,3,4,5])
#          output: [1,2,3,4,5]

my_array = [1,1,2,3,4,5]

def duplicate_numbers(list):
    dup_numbers = []

    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] == list[j]:
                dup_numbers.append(list[j])  

    return dup_numbers

def remove_duplicates(list):
    uniq_numbers = []

    for i in list:
        if i not in uniq_numbers:
            uniq_numbers.append(i)

    return uniq_numbers


print(duplicate_numbers(my_array))

print(remove_duplicates(my_array))