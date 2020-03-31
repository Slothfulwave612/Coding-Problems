## Detect a loop in linked list.

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
        Function to initialize the object of the class.

        Argument:
        self -- represents the object of the class.
        '''
        self.head = None

    def add_node(self, data):
        '''
        Function will add node to the linked list.

        Arguments:
        self -- represents the object of the class.
        data -- int, value to be inserted in the node.
        '''
        if self.head == None:
            self.head = Node(data)
        
        temp = self.head
        while temp.next != None:
            temp = temp.next

        temp.next = Node(data)

    def detect_loop(self):
        '''
        Function to detect the loop in the linked list.

        Argument:
        self -- represents the object of the class.
        '''
        if self.head == None:
            ## if the linked list is empty
            return
        
        slow_counter = self.head
        fast_counter = self.head

        while fast_counter != None:
            fast_counter = fast_counter.next

            if fast_counter == None:
                print('No loop found')
                return
            
            fast_counter = fast_counter.next
            slow_counter = slow_counter.next

            if fast_counter == slow_counter:
                print('Loop has been found')
                return
    
l_list = LinkedList()
l_list.add_node(20) 
l_list.add_node(4) 
l_list.add_node(15) 
l_list.add_node(10) 
   
# Create a loop for testing 
l_list.head.next.next.next.next = l_list.head
l_list.detect_loop()   
