## remove loop in linked list | 2nd approach

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
    a linked list.
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
        
    def find_loop(self):
        '''
        Function to find loop of in a linked list.

        Argument:
        self -- represents the object of the class.
        '''
        if self.head == None:
            ## if linked list is empty
            return
        
        fast_pointer = self.head
        slow_pointer = self.head

        while fast_pointer != None:
            fast_pointer = fast_pointer.next
            
            if fast_pointer == None:
                print('No loop found')
            
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next

            if fast_pointer == slow_pointer:
                self.remove_loop(slow_pointer)
                return

        print('No loop found')
        return
    
    def remove_loop(self, loop_pointer):
        '''
        Function to remove the loop from the linked list.

        Arguments:
        self -- represents the object of the class.
        loop_pointer -- node where fast and slow pointer met.
        '''
        head_pointer = self.head

        ptr = loop_pointer
        count = 1
        
        while ptr.next != loop_pointer:
            count += 1
            ptr = ptr.next

        ptr = self.head
        for i in range(count):
            ptr = ptr.next

        while ptr != head_pointer:
            ptr = ptr.next
            head_pointer = head_pointer.next

        while ptr.next != head_pointer:
            ptr = ptr.next
        
        ptr.next = None
    
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

# Driver program 
llist = LinkedList() 
llist.add_node(10) 
llist.add_node(4) 
llist.add_node(15) 
llist.add_node(20) 
llist.add_node(50) 
  
# Create a loop for testing 
llist.head.next.next.next.next.next = llist.head.next.next
  
llist.find_loop() 
  
print("Linked List after removing loop")
llist.traverse() 
