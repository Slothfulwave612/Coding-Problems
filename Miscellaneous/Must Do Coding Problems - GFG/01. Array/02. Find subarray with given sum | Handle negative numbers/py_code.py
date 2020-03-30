## Find subarray with given sum | Handle negative numbers

def find_subarray(array, length, req_sum):
    '''
    Function to find the subarray which will give the required sum.

    Arguments:
    array -- list, containing integers in unsorted order.
    length -- int, length of the array.
    req_array -- int, the required sum 

    Returns:
    the start and end index of the subarray
    '''
    map_dict = {}
    curr_sum = 0

    for i in range(length):
        curr_sum += array[i]

        if curr_sum == req_sum:
            return (0, i)
        
        if curr_sum - req_sum in map_dict:
            return(map_dict[curr_sum - req_sum] + 1, i)
        
        map_dict[curr_sum] = i
    
    return 0

array = [10, 2, -2, -20, 10]
req_sum = -10
result = find_subarray(array, len(array), req_sum)

if result == 0:
    print('No subarray found')
else:
    start, end = result[0], result[1]
    print(array[start: end+1])
    
