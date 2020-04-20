def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    row_dict = {}
    col_dict = {}
    m = len(matrix)
    n = len(matrix[0])
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                if row_dict.get(i) == None:
                    row_dict[i] = True
                if col_dict.get(j) == None:
                    col_dict[j] = True
    
    for i in row_dict.keys():
        for j in range(0, n):
            matrix[i][j] = 0
    print(matrix)
    for i in col_dict.keys():
        for j in range(0, m):
            matrix[j][i] = 0
    
    print(matrix)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeroes(matrix)
