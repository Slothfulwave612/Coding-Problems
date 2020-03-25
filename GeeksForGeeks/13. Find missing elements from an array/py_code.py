## Find missing element from an array.

def find_missing(array):
    '''
    This function will find all the missing elements from the array.

    Argument:
    array -- list, containing integer values.
    '''
    length = len(array) 

    for i in range(length):
        temp = array[i]

        if array[temp - 1] > 0:
            array[temp - 1] = 0
    
    for i in range(length):
        if array[i] != 0:
            print(i + 1, end=' ')
    
array = [1, 2, 3, 4, 4, 7, 7]
find_missing(array)
