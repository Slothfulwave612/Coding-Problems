## The K weakest rows in a matrix

def kWeakestRows(mat, k):
    '''
    The function makes a count of the number of 1 in each array of matrix
    And returns the required result

    Arguments:
    mat -- matrix of any shape
    k -- total number of weak array indices we need to display

    Returns:
    <list> -- list of k weakest rows
    '''

    weak_dict = {}

    for i in range(len(mat)):
        weak_dict[i] = mat[i].count(1)

    weak_array = sorted(weak_dict, key=weak_dict.get, reverse=False)

    return weak_array[:k]

mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]

k = 3

print(kWeakestRows(mat,k))