## 2D Sum

def two_d_sum(mat):
    '''
    Returns the required sum.

    Arguments:
    mat -- a square matrix

    Retuns:
    summ -- required sum from the matrix
    '''
    
    length = len(mat)
    summ = 0

    for i in range(length):
        for j in range(length):
            if i == 0 or i == length - 1:
                summ += mat[i][j]
            
            elif j == 0 or j == length - 1:
                summ += mat[i][j]

            elif i == j:
                summ += mat[i][j]
    
    return summ

mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

print(two_d_sum(mat))