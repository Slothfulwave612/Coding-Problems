## Find the length of linked list(recursive).

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize the object of the class.

        Arguments:
        self -- represents the object of the class.
        data -- int, value to be inserted in the node.
        '''
        self.data = data
        self.next = None

class LinkedList:
    '''
    a linked list class.
    '''

    def __init__(self):
        '''
        Function to initialize the object of linked list class.

        Argument:
        self -- represents the object of the class.
        '''
        self.head = None
    
    def add_node(self, data):
        '''
        Function to add node to the linked list.

        Arguments:
        self -- represents the object of the class.
        data -- int, value to be inserted in the node.
        '''
        if self.head == None:
            ## if linked list is empty
            self.head = Node(data)
            return
        
        temp = self.head
        while temp.next != None:
            temp = temp.next
        
        temp.next = Node(data)
    
    def traverse(self):
        '''
        Function to traverse the linked list.

        Argument:
        self -- represents the object of the class.
        '''
        if self.head == None:
            ## if linked list is empty
            return 

        temp = self.head
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        
    def find_length_recursive(self, node):
        '''
        Function to find length of a given linked list.

        Argument:
        self -- represents the object of the class.
        node -- the node in the linked list
        '''
        if node.next == None:
            ## if linked list is empty
            return 1

        return 1 + self.find_length_recursive(node.next)
        
    def get_count(self):
        '''
        Function to return find_length_recursive function to start the procees of counting.

        Argument:
        self -- represents the object of the class.
        '''
        if self.head == None:
            return 0

        return self.find_length_recursive(self.head)

l_list = LinkedList()

while True:
    print('\n1. Add a node.')
    print('2. Find Length.')
    print('3. Exit.\n')

    choice = int(input("Enter your choice:- "))

    if choice == 1:
        data = int(input("\nEnter a value:- "))
        l_list.add_node(data)
    
    elif choice == 2:
        l_list.traverse()
        length = l_list.get_count()
        print(f'\nThe length of the given linked list is: {length}')
    
    elif choice == 3:
        break
