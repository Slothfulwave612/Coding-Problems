## Array Number Product

def array_number_product(arr):
    '''
    The function returns required array output

    Arguments:
    arr -- an array of integers

    Returns:
    req_arr -- required array 
    '''

    result = arr[0]
    
    for i in range(1, len(arr)):
        result *= arr[i]
    
    req_arr = [result // x for x in arr]

    return req_arr

arr = [1, 2, 3, 4]
print(array_number_product(arr))