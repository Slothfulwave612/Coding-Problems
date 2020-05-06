'''
Insert and traverse a binary search tree.
'''

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize the Node class object.

        Arguments:
        self -- represents the object of the class.
        data -- int, data to be added to the node.
        '''
        self.left = None    ## left child
        self.right = None   ## right child
        self.data = data

def insert(root, data):
    '''
    Function to insert node to the tree.

    Arguments:
    root -- Node class object, root node for our tree.
    data -- int, data to be added to the node.
    '''
    if root.data:
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
    Function to traverse the tree.(inorder traversal).

    Arguments:
    root -- Node class object, root value of our tree
    '''
    if root:

        ## traversing left child
        traverse(root.left)

        ## printing value
        print(root.data, end=' ')

        ## traversing right child
        traverse(root.right)

root = Node(5)
insert(root, 12)
insert(root, 1)
insert(root, 7)
insert(root, 3)

traverse(root)
