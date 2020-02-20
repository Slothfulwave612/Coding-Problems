## Orignal Matrix from a Sparse Matrix

def original_matrix(sparse_mat):
    '''
    The function returns the original matrix out of a 3 tuple representation.

    Argument:
    sparse_mat -- the three tuple representation of a sparse matrix.

    Returns:
    orig_mat -- the original matrix.
    '''

    row_len = sparse_mat[0][0]      ## number of rows
    col_len = sparse_mat[0][1]      ## number of cols

    orig_mat = [[0 for i in range(col_len)] for j in range(row_len)]
    ## original matrix
    k = 1
    ## index for sparse_matrix
    
    for i in range(row_len):
        for j in range(col_len):
            if i == sparse_mat[k][0] - 1 and j == sparse_mat[k][1] - 1:
                orig_mat[i][j] = sparse_mat[k][2]
                k += 1
            else:
                orig_mat[i][j] = 0
    
    return orig_mat

sparse_mat = [[3, 2, 3], 
              [1, 2, 27], 
              [2, 1, 52], 
              [3, 2, 19]]

orig_mat = original_matrix(sparse_mat)

print(orig_mat)
