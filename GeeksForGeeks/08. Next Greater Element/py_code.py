## Next Greater Element

def next_greater_element(array):
    '''
    This function will print next greater element.

    Argument:
    array -- int, containing integer values.
    '''
    stack = []
    length = len(array)

    stack.append(array[0])

    for i in range(1, length):
        nxt = array[i]

        if stack != []:
            element = stack.pop()

            while element < nxt:
                print(f'{element} -- {nxt}')
                if stack == []:
                    break
                element = stack.pop()
            
            if element > nxt:
                stack.append(element)

        stack.append(nxt)

    for i in range(len(stack)):
        print(f'{stack[i]} -- -1')

array = [3, 12, 10, 2, 4, 5, 34, 17]
next_greater_element(array)
