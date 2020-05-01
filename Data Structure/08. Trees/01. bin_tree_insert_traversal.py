'''
Binary Tree Implementation in Python.
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
        self.data = data
        self.left = None    ## left child
        self.right = None   ## right child    

    def insert(self, data):
        '''
        Function to insert a node in the tree.

        Arguments:
        self -- represents the object of the class.
        data -- int, data to be added to the node.
        '''
        if self.data:
            if data < self.data:
                ## if data is smaller than root node value
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            
            elif data > self.data:
                ## if data is bigger than root node value
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

        else:
            ## if tree is empty 
            self.data = data
        
    def traverse(self):
        '''
        Function to traverse the binary tree.

        Argument:
        self -- represents the object of the class.
        '''
        if self.data:
            if self.left:
                self.left.traverse()
            print(self.data, end=' ')

            if self.right:
                self.right.traverse()
            # print(self.data, end='')

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.traverse()
