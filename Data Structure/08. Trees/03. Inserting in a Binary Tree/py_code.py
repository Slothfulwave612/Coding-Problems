'''
Inserting a node in a binary tree.
'''

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize the object of node class.

        Arguments:
        self -- represents the object of the class.
        data -- int, data to be added to the node.
        '''
        self.left = None    ## left child
        self.right = None   ## right child
        self.data = data    ## data value

def insert(root, data):
    '''
    Function to insert data to a binary tree.

    Arguments:
    root -- Node class object.
    data -- int, data to be added to the tree.
    '''
    if root:
        if data < root.data:
            if root.left == None:
                root.left = Node(data)
            else:
                insert(root.left, data)
        
        else:
            if root.right == None:
                root.right = Node(data)
            else:
                insert(root.right, data)

def traverse(root):
    '''
    Function to traverse the tree, in-order traversal.

    Argument:
    root -- Node class object.
    '''
    if root:

        ## visiting the left child
        traverse(root.left)

        ## printing the node value
        print(root.data, end=' ')

        ## visiting the right child
        traverse(root.right)

root = Node(2)
insert(root, 1)
insert(root, 3)
insert(root, -1)
insert(root, 5)

traverse(root)
