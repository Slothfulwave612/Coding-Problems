## 1-bit and 2-bit character

def isOneBitCharacter(bits):
    '''
    The function returns whether the array has 1 or 2 bit character at the end

    Arguments:
    bits -- an array of intergers having 0 and 1

    Returns:
    <bool> -- True: if the array has 1-bit character at the end
                  False: if the array has 2-bit character at the end 
    '''
    i = 0

    while i < len(bits) - 1:
        if bits[i] == 1:
            i += 1
            if i == len(bits) - 1:
                return False
        i += 1
    return True

bits1 = [1, 0, 0]
bits2 = [1, 1, 0, 1, 0]

print(isOneBitCharacter(bits1))
print(isOneBitCharacter(bits2))