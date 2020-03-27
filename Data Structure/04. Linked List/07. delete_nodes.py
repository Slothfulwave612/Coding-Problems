## function to delete a Linked List

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize the object of the node class.

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
        Function to initialize the object of the linked list class.

        Argument:
        self -- represents the object of the class.
        '''
        self.head = None
    
    def add_node(self, data):
        '''
        Function to add node to the linked list.

        Arguments:
        self -- represents the object of the class.
        data -- int, value to be inserted.
        '''
        if self.head == None:
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
            print('Empty Linked List')
            return 
        
        temp = self.head
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        print()
    
    def delete_all_nodes(self):
        '''
        Function deletes all node in the linked list one by one.

        Argument:
        self -- represents the object of the class.
        '''
        if self.head == None:
            print('Empty Linked List')
            return
        
        self.traverse()
        while self.head != None:
            next_node = self.head.next
            self.head = self.head.next
            next_node = None
            self.traverse()

l_list = LinkedList()

while True:
    print('\n1. Insert a node.')
    print('2. Delete nodes of linked list.')
    print('3. Exit\n')

    choice = int(input("Enter a choice:- "))

    if choice == 1:
        data = int(input("Enter a value:- "))
        l_list.add_node(data)
    
    elif choice == 2:
        l_list.delete_all_nodes()
    
    elif choice == 3:
        break
