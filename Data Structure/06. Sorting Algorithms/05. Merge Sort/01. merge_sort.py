## Merge Sort Implementation

def merge(array, front, mid, rare):
    '''
    This function will perform merging.

    Arguments:
    array -- list, containing integer values.
    front -- int, starting position of the array.
    mid -- int, middle position of the array.
    rare -- int, rare position of the array.
    '''
    left_array = array[front : mid + 1]
    right_array = array[mid + 1 : rare + 1]

    left_array_index = 0
    right_array_index = 0
    sorted_index = front

    while left_array_index < len(left_array) and right_array_index < len(right_array):
        if left_array[left_array_index] <= right_array[right_array_index]:
            array[sorted_index] = left_array[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_array[right_array_index]
            right_array_index += 1
        
        sorted_index += 1
    
    while left_array_index < len(left_array):
        array[sorted_index] = left_array[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    while right_array_index < len(right_array):
        array[sorted_index] = right_array[right_array_index]
        right_array_index += 1
        sorted_index += 1

def merge_sort(array, front, rare):
    '''
    This function will return a sorted array.

    Argument:
    array -- list, containing integer values in unsorted order.
    front -- int, starting position of the array.
    rare -- int, rare position of the array.

    Returns:
    array -- list, containing integer values in sorted order.
    '''
    if front < rare:
        mid = (front + rare) // 2

        merge_sort(array, front, mid)
        merge_sort(array, mid+1, rare)

        merge(array, front, mid, rare)
    
    return array

array = [10, 9, 3, 2, 4, 7, 5, 6, 8, 1]
print(f'Initial Array: {array}')

array = merge_sort(array, 0, len(array) - 1)
print(f'Sorted Array: {array}')
