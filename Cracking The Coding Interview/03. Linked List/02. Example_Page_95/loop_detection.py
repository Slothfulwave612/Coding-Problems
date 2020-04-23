'''
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list.
EXAMPLE
Input: A -> B -> C -> 0 -> E - > C
Output: C
'''

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize the Node class object.

        Arguments:
        self -- represents the object of the class.
        data -- int, 
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

        Argument:
        self -- represents the object of the class.
        '''
        self.head = None
    
    def add_node(self, data):
        '''
        Function to add node to the linked list.

        Arguments:
        self -- represents the object of the class.
        data -- int, the data to be added to the node.
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
        Function to detect loop.

        Argument:
        self -- represent the object of the class.

        Returns:
        data value where loop is found,
        else returns False.
        '''
        if self.head == None:
            ## if linked list is empty
            return
        
        slow_pointer = self.head
        fast_pointer = self.head
        
        while fast_pointer != None:
            fast_pointer = fast_pointer.next

            if fast_pointer == None:
                return False
            
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next

            if fast_pointer == slow_pointer:
                return fast_pointer.data

        if fast_pointer == None:
            return False

l_list = LinkedList()
l_list.add_node(20) 
l_list.add_node(4) 
l_list.add_node(15) 
l_list.add_node(10) 
   
# Create a loop for testing 
l_list.head.next.next.next.next = l_list.head
print(l_list.detect_loop())
