## Merge 3 Sorted Arrays

def merge_three_arrays(A, B, C):
    '''
    This function will merge two sorted arrays.

    Arguments:
    A -- list, containing integers values in sorted order.
    B -- list, containing integers values in unsorted order.
    C -- list, containing integers values in unsorted order.
    
    Returns:
    sorted_three -- list, containing integer values from A and B in sorted order.
    '''
    length_A, length_B, length_C = len(A), len(B), len(C)

    sorted_three = []

    index_A, index_B, index_C = 0, 0, 0

    while index_A != length_A and index_B != length_B and index_C != length_C:
        if A[index_A] < B[index_B] and A[index_A] < C[index_C]:
            sorted_three.append(A[index_A])
            index_A += 1
        elif C[index_C] < B[index_B] and C[index_A] < A[index_A]:
            sorted_three.append(C[index_C])
            index_C += 1
        else:
            sorted_three.append(B[index_B])
            index_B += 1
    
    while index_A != length_A:
        sorted_three.append(A[index_A])
        index_A += 1
    
    while index_B != length_B:
        sorted_three.append(B[index_B])
        index_B += 1
    
    while index_C != length_C:
        sorted_three.append(C[index_C])
        index_C += 1

    return sorted_three

A = [1, 2, 3, 4, 5] 
B = [2, 3, 4]
C = [4, 5, 6, 7]

sorted_three = merge_three_arrays(A, B, C)

print(sorted_three)
