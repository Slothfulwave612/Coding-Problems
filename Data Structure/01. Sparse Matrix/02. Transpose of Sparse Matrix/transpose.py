## Transpose of a Sparse Matrix

def transpose_sparse(sparse_mat):
    '''
    The function returns 3-tuple representation of a transposed sparse matrix.

    Arguments:
    sparse_mat -- 3-tuple representation of a sparse matrix

    Returns:
    trans_sparse_mat -- 3 tuple representation of a transposed sparse matrix
    '''
    trans_sparse_mat = [[0] * 3] * len(sparse_mat)

    for i in range(len(sparse_mat)):
        trans_sparse_mat[i] = [sparse_mat[i][1], sparse_mat[i][0], sparse_mat[i][2]]
    
    return trans_sparse_mat

sparse_mat = [[3, 2, 3], 
              [1, 2, 27], 
              [2, 1, 52], 
              [3, 2, 19]]

trans_sparse_mat = transpose_sparse(sparse_mat)

for i in range(len(trans_sparse_mat)):
    print(f'{trans_sparse_mat[i][0]} \t {trans_sparse_mat[i][1]} \t {trans_sparse_mat[i][2]}')
