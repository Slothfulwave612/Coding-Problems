'''
Maximum width of a binary tree.
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
        data -- int, data to be entered to the node.
        '''
        self.left = None
        self.right = None
        self.data = data
    
def insert(root, data):
    '''
    Function to insert data to the node.

    Arguments:
    root -- Node class object.
    data -- int, data to be entered to the node.
    '''
    if root:
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                insert(root.left, data)
        
        elif data > root.data:
            if root.right is None:
                root.right = Node(data)
            else:
                insert(root.right, data)

def traverse(root):
    '''
    Function to traverse to the tree.(in-order traversal)

    Argument:
    root -- represents the object of the class.
    '''
    if root:
        ## traverse the left child
        traverse(root.left)

        ## visit the node value
        print(root.data)

        ## traverse the right child
        traverse(root.right)

def height_of_tree(root):
    '''
    To calculate the height of the tree.

    Argument:
    root -- represents the object of the class.
    '''
    if root is None:
        return 0
    
    return height_of_tree(root.left) + 1 + height_of_tree(root.right)

def get_max_width(root, count, level):
    '''
    Function to get width for each level.

    Arguments:
    root -- Node class object.
    count -- list, that will contain how many nodes are there in each level.
    level -- int, level number
    '''
    if root is not None:
        count[level] += 1
        get_max_width(root.left, count, level+1)
        get_max_width(root.right, count, level+1)        

def max_width(root):
    '''
    Function to get the maximum width of the given tree.

    Argument:
    root -- represents the object of the class.
    '''
    height = height_of_tree(root)

    count = [0] * height

    level = 0

    get_max_width(root, count, level)

    return max(count)

root = Node(1)
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.right = Node(8) 
root.right.right.left = Node(6) 
root.right.right.right = Node(7)  

print(max_width(root))
