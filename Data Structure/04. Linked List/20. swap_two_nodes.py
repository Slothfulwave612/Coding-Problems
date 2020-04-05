## Swap two nodes in a linked list.

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize the Node class objects.

        Arguments:
        self -- represnts the object of the class.
        data -- int, data to be added to the node.
        '''
        self.data = data
        self.next = None
    
class LinkedList:
    '''
    a linked list class.
    '''

    def __init__(self):
        '''
        Function to initialize the Linked List object.

        Arguments:
        self -- represents the object of the class.
        '''
        self.head = None
    
    def add_node(self, data):
        '''
        Function to add node to the linked list.

        Argument:
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
        Function to traverse a linked list.

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
    
    def swap_nodes(self, first_data, second_data):
        '''
        Function to swap two nodes.

        Arguments:
        self -- represents the object of the class.
        first_data -- int, data from first node that is to be swapped.
        second_data -- int, data from second node that is to be swapped.
        '''
        if self.head == None:
            ## if linked list is empty
            return
        
        if first_data == second_data:
            return
        
        curr_X = self.head
        prev_X = None

        while curr_X != None and curr_X.data != first_data:
            prev_X = curr_X
            curr_X = curr_X.next
        
        curr_Y = self.head
        prev_Y = None

        while curr_Y != None and curr_Y.data != second_data:
            prev_Y = curr_Y
            curr_Y = curr_Y.next
        
        if curr_X == None or curr_X == None:
            return
        
        if prev_X != None:
            prev_X.next = curr_Y
        else:
            self.head = curr_Y
    
        if prev_Y != None:
            prev_Y.next = curr_X
        else:
            self.head = curr_X

        temp = curr_X.next
        curr_X.next = curr_Y.next
        curr_Y.next = temp
    
l_list = LinkedList()

while True:
    print('\n1. Add a node.')
    print('2. Traverse Linked List.')
    print('3. Swap nodes.')
    print('4. Exit.')

    choice = int(input("Enter a choice:- "))

    if choice == 1:
        data = int(input("Enter a value:- "))
        l_list.add_node(data)
    
    elif choice == 2:
        l_list.traverse()
    
    elif choice == 3:
        first_data = int(input("Enter data 1:- "))
        second_data = int(input("Enter data 2:- "))

        l_list.swap_nodes(first_data, second_data)
    
    elif choice == 4:
        break
