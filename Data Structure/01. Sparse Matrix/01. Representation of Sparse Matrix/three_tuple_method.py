## 3-Tuple Method

def three_tuple_method(mat):
    '''
    The function returns the 3-tuple representation of a given sparse matrix.

    Arguments:
    mat -- a 2D array of integer value(sparse matrix).

    Returns:
    <list> -- required 3-tuple representation in form of a matrix.
    '''

    row_len = len(mat)      ## total number of rows
    col_len = len(mat[0])   ## total number of cols

    non_zero = 0

    ## counting total number of non-zeros in matrix
    for i in range(row_len):
        non_zero += sum([1 for x in mat[i] if x != 0])

    ## creating a matrix which will store 3-tuple representation
    sparse_mat = [[0] * 3] * (non_zero + 1)
    k = 0
    ## index for sparse_mat

    sparse_mat[0] = [row_len, col_len, non_zero]
    ## adding number of rows, cols and non_zeros in the first row of sparse_mat

    for i in range(row_len):
        for j in range(col_len):
            if mat[i][j] != 0:  
                k += 1      
                sparse_mat[k] = [i+1, j+1, mat[i][j]]
    
    return sparse_mat

mat = [[0, -4, 5, 0, 1],
       [9, 0, 0, 2, 0],
       [0, 3, 0, 0, 0],
       [6, 0, 0, 0, 12]]

sparse_mat = three_tuple_method(mat)

for i in range(0, len(sparse_mat)):
    print(f'{sparse_mat[i][0]} \t {sparse_mat[i][1]} \t {sparse_mat[i][2]}')
