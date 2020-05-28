'''
Remove duplicates from sorted array.

Return the length of the array after the duplicates has been removed.
'''

def return_length(array):
    '''
    Function to return the length of the array
    after deleting the duplicates.

    Argument:
    array -- list, of sorted integers.

    Returns:
    int, the length after deleting the duplicate from the array.
    '''
    length = len(array)
    count = 0

    for i in range(1, length):
        if array[i] == array[i - 1]:
            count += 1
    
    return length - count

array_1 = [1, 1, 2]
print(return_length(array_1))

array_2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(return_length(array_2))
