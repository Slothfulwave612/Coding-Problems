## Maximum sum of 'k' consecutive elements in the array.

def sum_k(array, k):
    '''
    Function to find the sum of 'k' consecutive elements in the array.

    Argument:
    array -- list, containing integers.
    k -- int, number of consecutive elements.

    Return:
    ans -- int, max sum of 'k' consecutive elements
    '''
    if len(array) == 0 or k == 0:
        return 0
    if k > len(array):
        return 'Invalid'
    
    length = len(array)
    i, j = 0, 0
    ans, temp = array[0], array[0]

    while j != length - 1:
        if j - i + 1 < k:
            temp = max(temp, temp + array[j + 1])
            j += 1
        else:
            ans = max(temp, ans)
            temp -= array[i]
            i += 1

    ans = max(temp, ans)

    return ans

array = [100, 200, 300, 400]
k = 3
print(sum_k(array, k))
