## Move last element to front of a given Linked List.

class Node:
    '''
    a node class.
    '''
    
    def __init__(self, data):
        '''
        Function to initialize the Node class objects.

        Arguments:
        self -- represents the object of the class.
        data -- int, value to be added to the node.
        '''
        self.data = data
        self.next = None
    
class LinkedList:
    '''
    a linked list class.
    '''

    def __init__(self):
        '''
        Function to initialize the LinkedList class objects.

        Argument:
        self -- represents the object of the class.
        '''
        self.head = None
    
    def add_node(self, data):
        '''
        Function to add node to the linked list.

        Arguments:
        self -- represents the object of the class.
        data -- int, value to be added to the node.
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
        print()
    
    def first_and_last(self):
        '''
        Function to swap first and last element of the linked list.

        Argument:
        self -- represents the object of the class.
        '''
        if self.head == None or self.head.next == None:
            ## if linked list is empty
            return
        
        temp = self.head
        first = self.head

        while temp.next.next != None:
            temp = temp.next
        
        second_last = temp
        
        self.head = second_last.next
        second_last.next = first
        self.head.next = first.next
        second_last.next.next = None
    
l_list = LinkedList()

while True:
    print('\n1. Add a node.')
    print('2. Traverse Linked List.')
    print('3. Swap.')
    print('4. Exit.')

    choice = int(input("Enter choice:- "))

    if choice == 1:
        data = int(input("\nEnter a value:- "))
        l_list.add_node(data)
    
    elif choice == 2:
        l_list.traverse()
    
    elif choice == 3:
        l_list.first_and_last()
    
    elif choice == 4:
        break
