## Program to find the initials of a name.

def find_initials(name):
    '''
    Function to find initials from a name.

    Argument:
    name -- str, name of a person.
    '''
    name = name.strip()

    for i in range(len(name)):
        if i == 0:
            print(name[i].upper(), end=' ')
        
        elif name[i - 1] == ' ':
            print(name[i].upper(), end=' ')
    print()

name = 'abhishek kumar singh'
find_initials(name)
