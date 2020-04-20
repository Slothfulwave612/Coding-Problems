def rotate_matrix(matrix):
    '''
    Function to rotate the matrix by 90 degrees.

    Arguments:
    matrix -- list, a 2d array.

    Returns:
    matrix -- list, rotated 2d array.
    '''
    length = len(matrix)

    ## transpose the matrix
    for i in range(0, length):
        for j in range(i, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    ## swap elements in each rows
    for i in range(0, length):
        for j in range(0, length//2):
            matrix[i][j], matrix[i][length - j -1] = matrix[i][length - j -1], matrix[i][j]
