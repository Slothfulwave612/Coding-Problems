'''
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
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
        Function to initialize the Linked List class object.

        Argument:
        self -- represents the object of the class.
        '''
        self.head = None
    
    def add_node(self, data):
        '''
        Function to add node to the Linked List.

        Argument:
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
    
    def kth_node(self, k):
        '''
        Function to find the kth node from the last.

        Arguments:
        self -- represents the object of the class.
        k -- int, the kth value.

        Returns:
        int, the node data value.
        '''
        if self.head == None:
            ## if linked list is empty
            return
        
        temp = self.head
        length = 1

        while temp.next != None:
            length += 1
            temp = temp.next
        
        pos = length - k 
        temp = self.head
        count = 0

        if pos >= 0:
            while count != pos:
                count += 1
                temp = temp.next
                if temp == None:
                    return 0
        
            print(temp.data)
        
        else:
            print('Nopes'))


l_list = LinkedList()

while True:
    print('1. Add a node')
    print('2. Traverse the linked list.')
    print('3. Print kth node\'s data')
    print('4. Exit')

    choice = int(input("Enter your choice:- "))

    if choice == 1:
        print()
        data = int(input("Enter data:- "))
        l_list.add_node(data)
    
    elif choice == 2:
        print()
        l_list.traverse()
    
    elif choice == 3:
        print()
        k = int(input("Enter the value for k:- "))
        l_list.kth_node(k)
    
    elif choice == 4:
        break
