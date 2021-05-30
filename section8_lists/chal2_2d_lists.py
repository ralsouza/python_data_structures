# 2D lists
# Given 2D list calculate the sum of diagonal elements.

my_list = [[1,2,3],[4,5,6],[7,8,9]]
# sum_diagonal(my_list) --> returns 15

def sumDiagonal(a):
    
    diag_sum = 0
    
    for i in range(len(a)):
        
        diag_sum += a[i][i]