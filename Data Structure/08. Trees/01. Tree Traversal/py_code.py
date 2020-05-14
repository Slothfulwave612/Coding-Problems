'''
Tree Traversal: Pre-order, In-order, Post-order
'''

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize the node class object.

        Arguments:
        self -- represents the object of the class.
        data -- int, data to be added to the node.
        '''
        self.left = None        ## left child
        self.right = None       ## right child
        self.data = data        ## node value

def pre_order(root):
    '''
    Function to perform pre-order traversal.

    Argument:
    root -- Node class object, the root node or a parent node.
    '''
    
    if root:
        ## visiting the node value
        print(root.data, end=' ')

        ## visiting the left child
        pre_order(root.left)

        ## visiting the right child
        pre_order(root.right)

def in_order(root):
    '''
    Function to perform in-order traversal.

    Argument:
    root -- Node class object, the root node or a parent node.
    '''

    if root:
        ## visiting the left child
        in_order(root.left)
        
        ## visiting the node value
        print(root.data, end=' ')

        ## visiting the right child
        in_order(root.right)

def post_order(root):
    '''
    Function to perform post-order traversal.

    Argument:
    root -- Node class object, the root node or a parent node.
    '''

    if root:
        ## visiting the left child
        post_order(root.left)

        ## visiting the right child
        post_order(root.right)

        ## visiting the node value
        print(root.data, end=' ')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print('Pre-order Traversal: ', end='')
pre_order(root)
print()

print('In-order Traversal: ', end='')
in_order(root)
print()

print('Post-order Traversal: ', end='')
post_order(root)
print()
