## Assign Cookies

def num_cookies(g, s):
    '''
    The function returns number of children that will get the cookie.

    Arguments:
    g -- list of integers containing values of child's content.
    s -- list of integers containing values of size of cookies.

    Returns:
    child -- number of child that will get the cookie.
    '''
    g.sort()
    s.sort()

    cookie, child = 0, 0

    while child < len(g) and cookie < len(s):
        if g[child] <= s[cookie]:
            child += 1
        cookie += 1
    
    return child

g = [1, 2, 3]
s = [1, 1]

print(num_cookies(g, s))