## Count of elements which are not at the correct position

def count_occurence(array):
    '''
    Function to count number of time a number is not in 
    it's correct position.

    Argument:
    array -- list, containing integers.

    Returns:
    count -- int, total number of occurences where number was not in place.
    '''
    cpy_array = array.copy()

    cpy_array.sort()
    count = 0

    for i in range(len(array)):
        if cpy_array[i] != array[i]:
            count += 1
    
    return count

array_1 = [1, 2, 6, 2, 4, 5]
print(count_occurence(array_1))

array_2 = [1, 2, 3, 4]
print(count_occurence(array_2))
