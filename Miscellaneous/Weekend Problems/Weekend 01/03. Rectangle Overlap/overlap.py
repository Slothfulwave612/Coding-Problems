'''
Find if two rectangles overlap

Given two rectangles, find if the given two rectangles overlap or not.

Note that a rectangle can be represented by two coordinates, top left and bottom right. So mainly we are given following four coordinates.

l1: Top Left coordinate of first rectangle.
r1: Bottom Right coordinate of first rectangle.
l2: Top Left coordinate of second rectangle.
r2: Bottom Right coordinate of second rectangle.
'''

def overlap(l1, r1, l2, r2):
    '''
    Function to check wheter two rectangles overlap or not.

    Arguments:
    l1: Top Left coordinate of first rectangle.
    r1: Bottom Right coordinate of first rectangle.
    l2: Top Left coordinate of second rectangle.
    r2: Bottom Right coordinate of second rectangle.

    Returns:
    True -- if they overlap.
    False -- if they do.
    '''
    ## when one rectangle is in the left of another
    if l1[0] > r2[0] or l2[0] > r2[0]:
        return False
    if r2[1] > l1[1] or r1[1] > l2[1]:
        return False
    
    return True

l1 = (0, 10)
r1 = (10, 0)
l2 = (5, 5)
r2 = (15, 0)

print(overlap(l1, r1, l2, r2))
