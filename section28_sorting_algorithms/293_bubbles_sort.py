# Bubble Sort
# - Bubble sort is also referred as Sinking sort
# - We repeatedly compare each pair of adjacent items and swap them if
#   they are in the wrong order

def bubble_sort(custom_list):
    for i in range(len(custom_list)-1):
        for j in range(len(custom_list)-i-1):
            if custom_list[j] > custom_list[j+1]:
                custom_list[j], custom_list[j+1] = custom_list[j+1], custom_list[j]
    print(custom_list)

c_list = [2,1,7,6,5,3,4,9,8]

bubble_sort(c_list)