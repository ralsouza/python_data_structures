

my_list = [[1,2,3],[4,5,6],[7,8,9]]

def sum_diag(a):

       diag_sum = 0

       for i in range(len(a)):
              diag_sum += a[i][i]

       return diag_sum

print(sum_diag(my_list))