## Find length of the loop in linked list.

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize the object of the Node class.

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
        Function to initialize the object of LinkedList class.

        Arguments:
        self -- represents the object of the class.
        data -- int, value to be inserted in the node.
        '''
        self.head = None
    
    def add_node(self, data):
        '''
        Function to add node in the linked list.

        Arguments:
        self -- represents the object of the class.
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
    
    def count_loop_length(self):
        '''
        Function counts the length of the loop present in the node.

        Argument:
        self -- represents the object of the class.
        '''
        if self.head == None:
            ## if linked list is empty
            return
        
        slow_counter = self.head
        fast_counter = self.head
        counter = 0

        while fast_counter != None:
            fast_counter = fast_counter.next

            if fast_counter == None:
                print('No loop found')
                return
            
            fast_counter = fast_counter.next
            slow_counter = slow_counter.next

            if fast_counter == slow_counter:
                counter = 1
                break
        
        if fast_counter == None:
            print('No loop found')
            return    

        fast_counter = fast_counter.next
        while fast_counter != slow_counter:
            counter += 1
            fast_counter = fast_counter.next
        
        print(f'Length of loop: {counter}')
    
l_list = LinkedList()
l_list.add_node(20) 
l_list.add_node(4) 
l_list.add_node(15) 
l_list.add_node(10) 
   
# Create a loop for testing 
l_list.head.next.next.next.next = l_list.head
l_list.count_loop_length()
