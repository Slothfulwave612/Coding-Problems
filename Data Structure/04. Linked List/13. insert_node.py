## to insert a node in a linked list after nth index.

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize Node class object.

        Arguments:
        self -- represents the object of the class.
        data -- int, value to be contained by the node.
        '''
        self.data = data
        self.next = None

class LinkedList:
    '''
    a linked list class.
    '''
    
    def __init__(self):
        '''
        Function to initialize LinkedList class object.

        Argument:
        self -- represents the object of the class.
        '''
        self.head = None
    
    def add_node(self, data):
        '''
        Function to add node to the linked list.

        Arguments:
        self -- represents the object of the class.
        data -- int, value to be inserted by the node.
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
    
    def insert_node(self, pos, data):
        '''
        Function to insert a node after given index.

        Arguments:
        self -- represents the object of the class.
        pos -- int, the index after which the node is to be inserted.
        data -- int, the data to be inserted in the node.
        '''
        if self.head == None:
            ## if linked list is empty
            return
        
        temp = self.head
        count = 0

        while count != pos:
            count += 1
            temp = temp.next
            if temp == None:
                print('No index found')
                return
        
        temp_node = Node(data)
        temp_node.next = temp.next
        temp.next = temp_node

l_list = LinkedList()

while True:
    print('\n1. Add a node.')
    print('2. Insert a node.')
    print('3. Traverse the linked list.')
    print('4. Exit.\n')

    choice = int(input("Enter the choice:- "))

    if choice == 1:
        data = int(input("\nEnter a data:- "))
        l_list.add_node(data)
    
    elif choice == 2:
        data = int(input("Enter a data:- "))
        pos = int(input("Enter an index:- "))

        l_list.insert_node(pos, data)
    
    elif choice == 3:
        l_list.traverse()
    
    elif choice == 4:
        break
