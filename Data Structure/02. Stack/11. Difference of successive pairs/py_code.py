'''
Given a stack of integers, how do you check whether each successive pair of
numbers in the stack is consecutive or not. The pairs can be increasing or decreasing, and
if the stack has an odd number of elements, the element at the top is left out of a pair. For
example, if the stack of elements are [4, 5, -2, -3, 11, 10, 5, 6, 20], then the output should
be true because each of the pairs (4, 5), (-2, -3), (11, 10), and (5, 6) consists of
consecutive numbers.
'''

def successive_pairs(stack):
    '''
    Function to check whether each successive pair of numbers in 
    the stack is consecutive or not.

    Argument:
    stack -- list, of numbers.

    Returns:
    bool -- True, if correct
            False, otherwise
    '''
    length = len(stack)

    if length == 1 or length == 0:
        return False

    if length % 2 != 0:
        length -= 1
    
    for i in range(0, length, 2):
        if abs(stack[i] - stack[i+1]) != 1:
            return False
    
    return True


stack_1 = [4, 5, -2, -3, 11, 10, 5, 6, 20]
stack_2 = [1, 2, 4, 5, 8, 9, 101, 100, 77, 76]
stack_3 = [1, 2, 3, 4, 5, 6, 10]
stack_4 = [1, 0, 2, -2, 3, -3]

print(successive_pairs(stack_1))
print(successive_pairs(stack_2))
print(successive_pairs(stack_3))
print(successive_pairs(stack_4))
