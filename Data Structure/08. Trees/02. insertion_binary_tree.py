'''
Inserting nodes in a binary tree.
'''

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize object of Node class.

        Arguments:
        self -- represents the object of Node class.
        data -- int, data to be added to the node.
        '''
        self.left = None    ## left child 
        self.right = None   ## right child
        self.data = data    ## data

def insert(root, data):
    '''
    Function to insert node to the tree.

    Arguments:
    root -- Node object
    data -- int, data to be added to the node.
    '''
    queue = []
    queue.append(root)

    while len(queue) != 0:
        temp = queue.pop(0)

        if temp.left == None:
            temp.left = Node(data)
            break
        else:
            queue.append(temp.left)
        
        if temp.right == None:
            temp.right = Node(data)
            break
        else:
            queue.append(temp.right)

def traverse(root):
    '''
    in-order traversal

    Argument:
    root -- Node class object.
    '''
    if root:
        ## traverse left child
        traverse(root.left)

        ## printing data
        print(root.data, end=' ')

        ## traverse right child
        traverse(root.right)

root = Node(1)
insert(root, 2)
insert(root, 3)
insert(root, 4)
insert(root, 5)

traverse(root)

