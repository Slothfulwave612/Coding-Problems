## Delete and Remove loop in a linked list.

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize the Node class object.

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
        Function to initialize the LinkedList class object.

        Argument:
        self -- represents the object of the class.
        '''
        self.head = None
    
    def add_node(self, data):
        '''
        Function to add node to th linked list.

        Arguments:
        self -- represents the obejct of the class.
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
    
    def detect_loop(self):
        '''
        Function will delete the loop in the linked list.

        Argument:
        self -- represents the object of the class.
        '''
        if self.head == None:
            ## if the linked list is empty
            return

        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer != None:
            fast_pointer = fast_pointer.next

            if fast_pointer == None:
                print('No loop found')
                return
            
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next

            if fast_pointer == slow_pointer:
                self.remove_loop(slow_pointer)
                return
    
    def remove_loop(self, loop_node):
        '''
        Function removes the loop.

        Argments:
        self -- represents the object of the class.
        loop_node -- the node where slow_pointer and fast_pointer meet.
        '''

        head_pointer = self.head

        while True:
            ptr = loop_node

            while ptr.next != loop_node and ptr.next != head_pointer:
                ptr = ptr.next
            
            if ptr.next == head_pointer:
                break
            
            head_pointer = head_pointer.next
        
        ptr.next = None

        temp = self.head
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        print()
    
l_list = LinkedList()

l_list.add_node(10) 
l_list.add_node(4) 
l_list.add_node(15) 
l_list.add_node(20) 
l_list.add_node(50) 
  
# Create a loop for testing 
l_list.head.next.next.next.next.next = l_list.head.next.next
l_list.detect_loop()
