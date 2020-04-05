## Pairwise swap elements of a given linked list.(recursive)

class Node:
    '''
    a node class.
    '''
    
    def __init__(self, data):
        '''
        Function to initialize the Node class object.

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
        Function to initialize the Linked List class object.

        Arguments:
        self -- represents the object of the class.
        '''
        self.head = None
    
    def add_node(self, data):
        '''
        Function to add node to the linked list.

        Arguments:
        self -- represents the object of the class.
        data -- int, value to be added to the linked list.
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
    
    def swap_pairs(self):
        '''
        Function to swap a linked list pairwise.

        Argument:
        self -- represents the object of the class.
        '''
        if self.head == None:
            return
        
        return self.recursive_result(self.head)

    def recursive_result(self, pos):
        '''
        Function to swap a linked list pairwise.

        Argument:
        self -- represents the object of the class.
        '''
        
        if pos != None and pos.next != None:
            pos.data, pos.next.data = pos.next.data, pos.data
            return self.recursive_result(pos.next.next)
        
l_list = LinkedList()

while True:
    print('\n1. Add a node.')
    print('2. Traverse Linked List.')
    print('3. Swap Pairwise.')
    print('4. Exit.\n')

    choice = int(input("Enter a choice:- "))

    if choice == 1:
        data = int(input("\nEnter a value:- ")) 
        l_list.add_node(data)
    
    elif choice == 2:
        l_list.traverse()
    
    elif choice == 3:
        l_list.swap_pairs()
    
    elif choice == 4:
        break
