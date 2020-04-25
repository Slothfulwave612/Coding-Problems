'''
Find all prime numbers from 2 to n.

Algorithm Used:- Sieve of Eratosthenes
'''

def print_prime(n):
    '''
    Function to print all prime numbers from 2 to n.

    Argument:
    n -- int, the last limit.
    '''
    num_list = [True for i in range(n+1)]
    p = 2

    while p * p <= n:
        if num_list[p] == True:
            for i in range(p*p, n+1, p):
                num_list[i] = False
        
        p += 1
    
    for i in range(2, n+1):
        if num_list[i] == True:
            print(i, end=' ')
    print()

print_prime(50)
