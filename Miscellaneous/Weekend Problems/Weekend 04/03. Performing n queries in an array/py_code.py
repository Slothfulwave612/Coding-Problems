'''
Performing n queries in array.

1. Given an array of size N
2. Perform Q queries on it
    --> increment subarray[L,R] by 1
3. Array was initially empty.
4. At the end print the final elements of the array.

e.g. we have an empty array of 10 size(array with 10 zeros)
     increment subarray=[[1, 5], [5, 8], [0, 3], [7, 10]] by 1
     return the final result
'''

def perform_queries(array, operations):
    '''
    Function to perform operations on the given array.

    Arguments:
    array -- list, of numbers on which operations are to be performed.
    operations -- list, of subarray position [L, R] where we have to increment each element by 1.

    Returns:
    array -- list, our resultant list after the operations has been done.
    '''
    for subarray in operations:
        array[ subarray[0] ] += 1
        array[ subarray[1] + 1] -=1

    return array

array = [0] * 11
operations = [[1, 5], [5, 8], [0, 3], [7, 9]]

array = perform_queries(array, operations)

summ = 0

for i in range(len(array) - 1):    
    print(array[i] + summ, end=' ')
    summ += array[i]
print()
