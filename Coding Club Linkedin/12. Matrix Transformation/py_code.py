## Matrix Tranformation

def transformed_matrix(mat, num_rows, num_cols):
    '''
    The function transforms the given matrix into a desired format.

    Arguments:
    mat -- a 2D matrix.
    num_rows -- total number of rows in the matrix.
    num_cols -- total number of columns in the matrix.

    Returns:
    trans_mat -- the required transformed matrix.
    '''

    trans_mat = [[0 for cols in range(num_cols)] for rows in range(num_rows)]

    for row in range(num_rows):
        for col in range(num_cols):
            trans_mat[row][col] = mat[col][row]
    
    top, bottom = 0, num_rows - 1

    while top < bottom:
        trans_mat[top], trans_mat[bottom] = trans_mat[bottom], trans_mat[top]
        top += 1
        bottom -= 1

    return trans_mat

mat1 = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

num_rows1, num_cols1 = len(mat1), len(mat1[0])

mat2 = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]
num_rows2, num_cols2 = len(mat2), len(mat2[0])

trans_mat1 = transformed_matrix(mat1, num_rows1, num_cols1)
trans_mat2 = transformed_matrix(mat2, num_rows2, num_cols2)

for i in range(num_rows1):
    for j in range(num_cols1):
        print(trans_mat1[i][j], end=' ')
    print()

print()

for i in range(num_rows2):
    for j in range(num_cols2):
        print(trans_mat2[i][j], end=' ')
    print()