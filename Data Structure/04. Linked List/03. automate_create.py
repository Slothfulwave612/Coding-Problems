## Creating and appending nodes in a linked list and printing the values.

class Node:
    '''
    A node class.
    '''

    def __init__(self, data):
        '''
        Function to intilize the node object.

        Arguments:
        self -- represents the object of the class.
        data -- int, values to be appended in the node.
        '''
        self.data = data
        self.next = None

class LinkedList:
    '''
    a linked list class.
    '''

    def __init__(self):
        '''
        Function to initialize linked list object.

        Argument:
        self -- represents the object of the class.
        '''
        self.head = None

    def add_node(self, data):
        '''
        Function to add nodes in a linked list.

        Arguments:
        self -- represents the object of the class.
        data -- int, the value to be added in the linked list.
        '''
        if self.head == None:
            ## if linked list is empty.
            self.head = Node(data)
        else:
            temp = self.head
            
            while temp.next != None:
                temp = temp.next

            temp.next = Node(data)
    
    def traverse_llist(self):
        '''
        Function will traverse the linked list.

        Argument:
        self -- represents the object of the class.
        '''
        temp = self.head

        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        print()
    
l_list = LinkedList()

while True:
    print('\n1. Enter Data')
    print('2. Display Linked List')
    print('3. Exit')

    choice = int(input("\nEnter Your Choice:- "))

    if choice == 1:
        data = int(input("\nEnter Data:- "))
        l_list.add_node(data)
    
    elif choice == 2:
        l_list.traverse_llist()
    
    elif choice == 3:
        break
