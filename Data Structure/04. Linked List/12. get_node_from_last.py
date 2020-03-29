## Get nth node from the end.

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize the object of Node class.
        
        Arguments:
        self -- represents the object of the class.
        data -- int, the value to be added to the node.
        '''
        self.data = data
        self.next = None

class LinkedList:
    '''
    a linked list.
    '''

    def __init__(self):
        '''
        Function to initialize the object of LinkedList class.

        Argument:
        self -- represents the object of the class.
        '''
        self.head = None
    
    def add_node(self, data):
        '''
        Function to add node to the linked list.

        Arguments:
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
    
    def traverse_node(self):
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
    
    def get_node(self, n):
        '''
        Function to get the nth from the last in the linked list.

        Arguments:
        self -- represents the object of the class.
        n -- int, the node position from the last.

        Returns:
        temp.data -- the value at nth node from the last.
        '''
        if self.head == None:
            return
        
        temp = self.head
        length = 0

        while temp.next != None:
            length += 1
            temp = temp.next
        
        pos = length - n + 1
        temp = self.head
        count = 0

        while count != pos:
            count += 1
            temp = temp.next
            if temp == None:
                return 0
        
        return temp.data

l_list = LinkedList()

while True:
    print('\n1. Add a node.')
    print('2. Find node.')
    print('3. Exit\n')

    choice = int(input("Enter choice :- "))

    if choice == 1:
        data = int(input("\nEnter value :- "))
        l_list.add_node(data)
    
    elif choice == 2:
        l_list.traverse_node()
        n = int(input("\nEnter node value:- "))
        result = l_list.get_node(n)
        if result == 0:
            print('Node not found')
        else:
            print(result)
        
    elif choice == 3:
        break
