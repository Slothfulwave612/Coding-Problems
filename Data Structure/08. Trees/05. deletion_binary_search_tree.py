'''
Deletion: Binary Tree
'''

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize Node class objects.

        Arguments:
        self -- represents the object of the class.
        data -- int, data to be added to the node.
        '''
        self.left = None        ## left child
        self.right = None       ## right child
        self.data = data        ## node's data
    
def insert(root, data):
    '''
    Function to insert node in a tree.

    Argument:
    root -- Node class object
    data -- int, data to be added to the node.
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

    else:
        root.data = Node(data)

def traverse(root):
    '''
    Function to traverse the tree. (in-order traverse)

    Argument:
    root -- Node class object.
    '''
    if root:

        ## traverse the left child
        traverse(root.left)

        ## visiting the node value
        print(root.data, end=' ')

        ## traverse the right child
        traverse(root.right)

def min_value(node):
    '''
    Function for finding minimum value in right sub tree.

    Argument:
    node -- Node class object.
    '''
    current = node

    while current.left != None:
        current = current.left
    
    return current

def delete(root, data):
    '''
    Function to remove the node.

    Arguments:
    root -- Node class object.
    data -- int, data to be deleted
    ''' 
    if root == None:
        return None
    
    if data < root.data:
        root.left = delete(root.left, data)
    
    elif data > root.data:
        root.right = delete(root.right, data)
    
    else:
        if root.left == None:
            temp = root.right
            root = None
            return temp

        elif root.right == None:
            temp = root.left
            root = None
            return temp
        
        temp = min_value(root.right)

        root.data = temp.data

        root.right = delete(root.right, temp.data)
    
    return root

root = Node(50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

print(f'Traversal: ', end='')
traverse(root)
print()
print()

print('Deleting 20')
delete(root, 20)
print(f'Traversal: ', end='')
traverse(root)
print()
print()

print('Deleting 30')
delete(root, 30)
print(f'Traversal: ', end='')
traverse(root)
print()
print()

print('Deleting 50')
delete(root, 50)
print(f'Traversal: ', end='')
traverse(root)
print()
print()
