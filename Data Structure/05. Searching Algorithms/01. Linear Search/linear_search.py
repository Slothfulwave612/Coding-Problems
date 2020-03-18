## Linear Search

def linear_search(array, target):
    '''
    Using linear search implementation, searching for a number in the list.

    Arguments:
    array -- list
    target -- number to be found in the list

    Returns:
    index -- if number is found, index of the number is returned
    -1 -- if number is not present
    '''
    for index in range(len(array)):
        if array[index] == target:
            return index
    return -1

array = [1, 3, 6, 2, 4, 5]
target = 6
index = linear_search(array, target)

if index != -1:
    print(index + 1)
else:
    print('Number not present')
