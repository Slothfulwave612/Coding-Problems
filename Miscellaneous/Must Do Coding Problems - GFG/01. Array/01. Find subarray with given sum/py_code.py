## Find subarray with given sum.

def find_subarray(array, length, req_sum):
    '''
    Function finds out the the subarray which gives the required sum.

    Arguments:
    array -- list, containing integers in unsorted order.
    length -- int, the length of the array.
    req_sum -- int, the required sum that is to be computed.

    Returns:
    start -- int, the starting index of the subarray.
    i-1 -- int, the ending index of the subarray.
    '''
    start = 0
    i = 1
    curr_sum = array[0]

    while i != length:
        while curr_sum > req_sum and start < i - 1:
            curr_sum -= array[start]
            start += 1
        
        if curr_sum == req_sum:
            return (start, i-1)
        
        if i < length:
            curr_sum += array[i]
            i += 1
    
    return 0

array = [1, 4, 20, 3, 10, 5]
req_sum = 33

result = find_subarray(array, len(array), req_sum) 

if result == 0:
    print('No subarray found')
else:
    start, end = result[0], result[1]
    print(array[start:end+1])
