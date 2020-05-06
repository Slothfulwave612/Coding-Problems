'''
Searching in a binary search tree.
'''

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize the Node class objects.

        Arguments:
        self -- represents the object of the class.
        data -- int, data to be added to the node.
        '''
        self.left = None    ## left child
        self.right = None   ## right child
        self.data = data    ## data value
    
def insert(root, data):
    '''
    Function to insert node to the tree.

    Arguments:
    root -- Node object, root of our tree 
    data -- int, data to be added to the node.
    '''
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
    Function to traverse the tree(inorder traversal).

    Arguments:
    root -- Node class object, representing root node.
    '''
    if root:
        
        ## traversing left child
        traverse(root.left)

        ## printing node value
        print(root.data, end=' ')

        ## traversing right child
        traverse(root.right)

def search(root, key):
    '''
    Function to search the key in the tree.

    Arguments:
    root -- Node object, root of our tree.
    key -- int, key to be searched.
    '''
    if root is None or root.data == key:
        return root.data
    
    if key < root.data:
        return search(root.left, key)
    
    return search(root.right, key)

root = Node(5)
insert(root, 12)
insert(root, 1)
insert(root, 7)
insert(root, 3)

traverse(root)
print()

print(search(root, 1))
