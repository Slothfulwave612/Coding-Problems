'''
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. lf x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5)
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
'''

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize the Node class objects.

        Arguments:
        self -- represents the object of the class.
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
        Function to initialize the Linked List class objects.

        Argument:
        self -- represents the object of the class.
        '''
        self.head = None
    
    def add_node(self, data):
        '''
        Function to add node to linked list.

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
        
    def traverse(self):
        '''
        Function to traverse the linked list.

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
    
    def partition(self, pivot_value):
        '''
        Function to perform the required partitions.

        Argument:
        self -- represent the object of the class.
        pivot_value -- int, the pivot value
        '''
        if self.head == None:
        ## if linked list is empty
            return

        low_list = LinkedList()
        high_list = LinkedList()
        temp = self.head

        while temp != None:
            if temp.data < pivot_value:
                low_list.add_node(temp.data)
            else:
                high_list.add_node(temp.data)
            
            temp = temp.next

        temp = low_list.head
        while temp.next != None:
            temp = temp.next
        
        temp.next = high_list.head

        low_list.traverse()

l_list = LinkedList()

while True:
    print()
    print('1. Add a node')
    print('2. Perform partition.')
    print('3. Exit')

    choice = int(input("Enter the choice:- "))
    print()

    if choice == 1:
        data = int(input("Enter the data:- "))
        l_list.add_node(data)

    elif choice == 2:
        l_list.traverse()
        pivot_value = int(input("Enter pivot value:- "))
        l_list.partition(pivot_value)
    
    elif choice == 3:
        break
