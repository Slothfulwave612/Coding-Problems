## Odd Even Array

def odd_even_array(num):
    '''
    Fill the array first with odd numbers then with even numbers

    Arguments:
    num -- integer value

    Returns:
    req_array -- the array having odd and even numbers in their required place
    '''
    count, req_array = 1, []

    while count != 0:
        req_array.append(count)
        if count % 2 == 0:
            count -= 2
        else:
            count += 2

        if count == num:
            req_array.append(count)
            count -= 1
        
        elif count == num - 1:
            req_array.append(count)
            count += 1
    
    return req_array

num = 16
print(odd_even_array(num))