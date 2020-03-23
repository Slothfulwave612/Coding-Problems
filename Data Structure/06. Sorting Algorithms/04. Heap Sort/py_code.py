## Heap Sort Implementation

def heapify(array, i, length):
    '''
    This function builds a max heap.

    Arguments:
    array -- list, containing integer values.
    i -- int, position in the array.
    '''
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < length and array[left_child] > array[largest]:
        largest = left_child
    
    if right_child < length and array[right_child] > array[largest]:
        largest = right_child
    
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, largest, length)

def heap_sort(array):
    '''
    This function performs heap sort.

    Argument:
    array -- list, containing integer values in unsorted order.

    Returns:
    array -- list, containing integer values in sorted order.
    '''
    length = len(array)

    for i in range((length-1) // 2, -1, -1):
        heapify(array, i, length)
    
    for i in range(length - 1, -1, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, 0, i)

    return array

array = [12, 11, 13, 5, 6, 7]
print(f'Initial Array: {array}')

array = heap_sort(array)
print(f'Sorted Array: {array}')
