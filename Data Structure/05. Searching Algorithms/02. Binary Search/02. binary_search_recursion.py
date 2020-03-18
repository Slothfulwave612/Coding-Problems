## Binary Search Implementation(Recursion)

def bin_search(array, target, front, rare):
    '''
    A recursive function that will search for the target value.

    Arguments:
    array -- sorted list, containing interger.
    target -- int, number to be searched.
    mid -- int, the middle position in the array.
    front -- int, the front position in the array.
    rare -- int, the rare position in the array.

    Returns:
    mid -- int, the position of that number in the array.
    -1 -- if the number is not present in the array.
    '''
    if rare >= front:
        mid = (rare + front) // 2

        if array[mid] == target:
            return mid
        
        elif array[mid] > target:
            return bin_search(array, target, front, mid - 1)
        
        elif array[mid] < target:
            return bin_search(array, target, mid + 1, rare)

    else:
        return -1

array = [1, 2, 3, 4, 5]
target = 4

index = bin_search(array, target, 0, len(array) - 1)

if index != -1:
    print(index + 1)
else:
    print('Number not present')
