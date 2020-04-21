'''
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
Input: the node c from the linked list a - >b- >c - >d - >e- >f
Result: nothing is returned, but the new linked list looks like a - >b- >d - >e- >f
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
        data -- int, the data to be added to the node.
        '''
        self.data = data
        self.next = None
    
class LinkedList:
    '''
    a linked list class.
    '''

    def __init__(self):
        '''
        Function to initialize the Linked List class objects.

        Argument:
        self -- represents the obejct of the class.
        '''
        self.head = None
    
    def add_node(self, data):
        '''
        Function to add node to the linked list.

        Arguments:
        self -- represents the object of the class.
        data -- int, data to be added to the node.
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
        Function will traverse the linked list.

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
    
    def remove_middle(self):
        '''
        Function will remove the middle element from the linked list.

        Argument:
        self -- represents the object of the linked list.
        '''
        if self.head == None:
            ## if linked list is empty
            return
        
        slow_pointer = self.head
        fast_pointer = self.head
        prev = None

        if slow_pointer.next == None:
            self.head = None
            return

        while fast_pointer.next != None:
            fast_pointer = fast_pointer.next

            if fast_pointer.next == None:
                break
                
            fast_pointer = fast_pointer.next
            prev = slow_pointer
            slow_pointer = slow_pointer.next
        
        if prev == None:
            self.head = fast_pointer
            return
        del_node = prev.next
        prev.next = del_node.next
        del del_node


l_list = LinkedList()

while True:
    print()
    print('1. Add a node')
    print('2. Traverse the linked list')
    print('3. Remove the middle element')
    print('4. Exit')

    choice = int(input("Enter your choice:- "))

    if choice == 1:
        data = int(input("Enter the data:- "))
        l_list.add_node(data)
    
    elif choice == 2:
        l_list.traverse()
    
    elif choice == 3:
        l_list.remove_middle()
    
    elif choice == 4:
        break
