'''
Tree Traversal:
1. Pre-order traversal
2. In-order traversal
3. Post-order traversal
'''

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize object of Node class.

        Argument:
        self -- represents the object of the class.
        '''
        self.left = None
        self.right = None
        self.data = data
    
def pre_order(root):
    '''
    Function for pre-order traversal.

    Argument:
    root -- Node object, root of our tree.
    '''
    if root:
        ## printing the parent value
        print(root.data, end=' ')

        ## traverse the left child
        pre_order(root.left)

        ## traverse the right child
        pre_order(root.right)

def in_order(root):
    '''
    Function for in-order traversal.

    Argument:
    root -- Node object, root of our tree.
    '''
    if root:

        ## traverse the left child
        in_order(root.left)

        ## print the value
        print(root.data, end=' ')

        ## traverse the right child
        in_order(root.right)

def post_order(root):
    '''
    Function for post-order traversal.

    Argument:
    root -- Node object, root of out tree.
    '''
    if root:

        ## traverse the left child
        post_order(root.left)

        ## traverse the right child
        post_order(root.right)

        ## print the data 
        print(root.data, end=' ')
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print('Pre-order:', end='')
pre_order(root)
print()

print('In-order:', end='')
in_order(root)
print()

print('Post-order:', end='')
post_order(root)
print()
