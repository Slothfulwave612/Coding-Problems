'''
Example: Print all positive integer solutions to the equation 
                a^3 + b^3 = c^3 + d^3
where a, b, c and d are integers between 1 and 1000.
'''

def find_val():
    '''
    Function finds required value for a, b, c and d
    which satisfies the equations.
    '''
    n = 1000
    hash_map = {}

    for c in range(1, n+1):
        for d in range(1, n+1):
            result = pow(c, 3) + pow(d, 3)
            hash_map[result] = (c,d)

    for a in range(1, n+1):
        for b in range(1, n+1):
            result = pow(a, 3) + pow(b, 3)
            if hash_map.get(result):
                print(a, b, hash_map[result][0], hash_map[result][1])

find_val()
