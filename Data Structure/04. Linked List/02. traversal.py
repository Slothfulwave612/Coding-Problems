## To traverse a linked list

class Node:
    '''
    This is a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize the node object.

        Arguments:
        self -- represents the object of the class.
        data -- int, value to be inserted in the node.
        '''
        self.data = data
        self.next = None

class LinkedList:
    '''
    Linked List class.
    '''

    def __init__(self):
        '''
        Function to initialize the LinkedList object.

        Arguments:
        self -- represents the object of the class.
        '''
        self.head = None

    def traverse_list(self):
        '''
        Function to traverse the linked list.

        Argument:
        self -- represents the object of the class.
        '''
        temp = self.head

        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        print()

l_list = LinkedList()

l_list.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

l_list.head.next = second
## conection from first node to second node

second.next = third
## conection from second node to third node

third.next = fourth
## conection from third node to fourth node

l_list.traverse_list()
## traversing the list and printing the values
