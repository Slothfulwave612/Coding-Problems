## Find the middle of a given linked list

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize the object of node class.

        Arguments:
        self -- represents the object of the class.
        data -- int, value to be appended in the node.
        '''
        self.data = data
        self.next = None
    
class LinkedList:
    '''
    a linked list class.
    '''
    
    def __init__(self):
        '''
        Function to initialize the object of Linked List class.

        Argument:
        self -- represents the object of the class.
        '''
        self.head = None

    def add_node(self, data):
        '''
        Function to insert a node in the linked list.

        Arguments:
        self -- represents the object of the class.
        data -- int, value to be appended in the linked list.
        '''
        if self.head == None:
            ## if the linked list is empty
            self.head = Node(data)
        else:
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
        temp = self.head

        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        print()
    
    def find_middle(self):
        '''
        Function finds the middle of the linked list.

        Argument:
        self -- represents the object of the class.

        Returns:
        slow_pointer.data -- int, the middle value of the linked list.
        '''
        if self.head == None:
            return

        self.traverse()
        ## shows all element in the linked list

        fast_pointer = self.head
        slow_pointer = self.head

        while fast_pointer != None and fast_pointer.next != None:
            fast_pointer = fast_pointer.next.next

            if fast_pointer == None:
                return slow_pointer

            slow_pointer = slow_pointer.next
        
        return slow_pointer

l_list = LinkedList()

while True:
    print('\n1. Enter Data')
    print('2. Find Middle Element.')
    print('3. Exit')

    choice = int(input('\nEnter Your Choice :- '))

    if choice == 1:
        data = int(input('\nEnter the data:- '))
        l_list.add_node(data)
    
    elif choice == 2:
        mid = l_list.find_middle()
        print(f'The middle element is {mid}')
    
    elif choice == 3:
        break
