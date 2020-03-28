## Find the length of linked list

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize Node class objects.

        Arguments:
        self -- represents the object of the class.
        data -- int, value to be inserted to the node.
        '''
        self.data = data
        self.next = None

class LinkedList:
    '''
    a linked list class.
    '''

    def __init__(self):
        '''
        Function to initialize LinkedList object.

        Argument:
        self -- represents the object of the class.
        '''
        self.head = None
    
    def add_node(self, data):
        '''
        Function to add node to the linked list.

        Arguments:
        self -- represents the object of the class.
        data -- int, value to be inserted to the node.
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
            print("Empty Linked List")
            return
        
        temp = self.head    
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def find_length(self):
        '''
        Function counts the length of the linked list.

        Argument:
        self -- represents the object of the class.

        Returns:
        length -- int, the length of the linked list.
        '''
        if self.head == None:
            print('Empty Linked List')
            return
        
        length = 0
        temp = self.head
        
        while temp != None:
            length += 1
            temp = temp.next
        
        return length

l_list = LinkedList()

while True:
    print('\n1. Add a node.')
    print('2. Length of the Linked List.')
    print('3. Exit.\n')

    choice = int(input("Enter the choice:- "))

    if choice == 1:
        data = int(input("\nEnter the data:- "))
        l_list.add_node(data)
    
    elif choice == 2:
        l_list.traverse()
        length = l_list.find_length()
        print(f'\nThe length of the Linked List is: {length}')
    
    elif choice == 3:
        break
