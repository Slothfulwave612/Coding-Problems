## reverse a linked list.

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

        Arguments:
        self -- represents the object of the class.
        '''
        self.head = None
    
    def add_node(self, data):
        '''
        Function to add node in the linked list.

        Arguments:
        self -- represents the object of the class.
        data -- int, data to be added to the node.
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
    
    def reverse_list(self):
        '''
        Function to reverse the linked list.

        Argument:
        self -- represents the object of the class.
        '''
        if self.head == None:
            ## if linked list is empty
            return
        
        prev = None
        curr = self.head
        nxt = None
    
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        self.head = prev

l_list = LinkedList()

while True:
    print('\n1. Add a node.')
    print('2. Traverse Linked List.')
    print('3. Reverse the Linked List.')
    print('4. Exit.')

    choice = int(input("\nEnter the choice:- "))

    if choice == 1:
        data = int(input("Enter a data:- "))
        l_list.add_node(data)
    
    elif choice == 2:
        l_list.traverse()
    
    elif choice == 3:
        l_list.reverse_list()
    
    elif choice == 4:
        break
