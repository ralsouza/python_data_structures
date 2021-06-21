# Insertion Sort
# - Divide the given array into two parts
# - Take first element from unsorted array and find it's correct position in sorted array
# - Repeat until unsorted array is empty

def insertion_sort(custom_list):
    for i in range(1,len(custom_list)):
        key = custom_list[i]
        j = i - 1
        while j >= 0 and key < custom_list[j]:
            custom_list[j+1] = custom_list[j]
            j -= 1
        custom_list[j+1] = key
    print(custom_list)
 
c_list = [2,1,7,6,5,3,4,9,8]

insertion_sort(c_list)