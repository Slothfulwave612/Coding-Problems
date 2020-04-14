'''
Given two sorted arrays, find the number of elements in common. 
The arrays are the same length and each has all distinct elements.
'''
def find_common(array_1, array_2):
    '''
    Function to find common elements in the 
    two sorted arrays.

    Arguments:
    array_1 -- list
    array_2 -- list
    '''
    index_1, index_2 = 0, 0
    ## index for array_2

    while index_1 != len(array_1):
        if array_1[index_1] > array_2[index_2]:
            index_2 += 1
        
        elif array_1[index_1] == array_2[index_2]:
            print(array_1[index_1])
            index_1 += 1
        
        else:
            index_1 += 1
        
array_1 = [13, 27, 35, 40, 49, 55, 59]
array_2 = [17, 35, 39, 40, 55, 58, 60]

find_common(array_1, array_2)
