# Selection Sort
# In case of selection we repeatedly find the minimum element and 
# move it to the sorted part of array to make unsorted part sorted.

def selection_sort(custom_list):
    for i in range(len(custom_list)):
        min_index = i
        for j in range(i+1,len(custom_list)):
            if custom_list[min_index] > custom_list[j]:
                min_index = j
        custom_list[i], custom_list[min_index] = custom_list[min_index], custom_list[i]
    print(custom_list)

c_list = [2,1,7,6,5,3,4,9,8]

selection_sort(c_list)