## Create a linked list

class Node:
    '''
    This is a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize the node object.

        Arguments:
        self -- represents the object.
        data -- int, value to be inserted in the linked list.
        '''
        self.data = data
        self.next = None

class LinkedList:
    '''
    Linked list class contains a node object.
    '''

    def __init__(self):
        self.head = None

l_list = LinkedList()

l_list.head = Node(1)
second = Node(2)
third = Node(3)
## the three nodes of linked list
## head pointing to the first node having value 1

l_list.head.next = second
second.next = third

