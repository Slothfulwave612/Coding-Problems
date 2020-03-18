## Binary Search Implementation

def binary_search(array, target):
    '''
    To search for a number in an array using Binary Search.

    Arguments:
    array -- sorted list
    target -- the integer to be found in the array

    Returns:
    mid -- the index of the number present in the array, if number is present in the array.
    -1 -- if the number is not present.
    '''
    front = 0 
    rare = len(array) - 1

    while front <= rare:
        mid = (front + rare) // 2

        if array[mid] == target:
            return mid
        
        elif array[mid] > target:
            rare = mid - 1
        
        elif array[mid] < target:
            front = mid + 1
    
    return -1

array = [10, 21, 30, 41, 55, 63, 66]
target = 41

index = binary_search(array, target)

if index != -1:
    print(index + 1)
else:
    print('Number not present')
