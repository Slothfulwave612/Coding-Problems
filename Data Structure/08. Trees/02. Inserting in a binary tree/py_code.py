'''
Inserting a node in a binary tree.
'''

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize the node class objects.

        Arguments:
        self -- represents the object of the class.
        data -- int, data to be added to the node.
        '''
        self.left = None        ## left child
        self.right = None       ## right child
        self.data = data        ## node value

def insert(root, data):
    '''
    Function to insert a node in the binary tree.

    Arguments:
    root -- represents the object of the class.
    data -- int, data to be added to the tree.
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
    Function to traverse the tree; in-order traversal.

    Argument:
    root -- Node class object, represents root node or a parent node or leaf node.
    '''
    if root:

        ## visiting the left child
        traverse(root.left)

        ## printing the data value
        print(root.data, end=' ')

        ## visiting the right child
        traverse(root.right)

root = Node(1)
insert(root, 2)
insert(root, 3)
insert(root, 4)
insert(root, 5)

traverse(root)
