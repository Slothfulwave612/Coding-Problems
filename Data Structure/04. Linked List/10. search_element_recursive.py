## Search an element in the linked list
## Return True if the element is present 
## False if it is not present

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize Node class objects.

        Arguments:
        self -- represents the object of the class.
        data -- int, value to be inserted to the node.
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
        data -- int, value to be inserted to the node.
        '''
        if self.head == None:
            ## if the linked list is empty
            self.head = Node(data)
            return
        
        temp = self.head
        while temp.next != None:
            temp = temp.next

        temp.next = Node(data)
    
    def traverse(self):
        '''
        Function to traverse the given linked list.

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
    
    def search_element(self, node, element):
        '''
        Function to search the element.

        Arguments:
        self -- represents the object of the class.
        node -- represent the particular node of the linked list.
        element -- int, the value to be searched
        '''
        if node.data == element:
            return True
            
        if node.next == None:
            return False
        
        return self.search_element(node.next, element)
    
    def get_element(self):
        '''
        Funtion to start the process of searching.

        Argument:
        self -- represents the object of the class.
        '''
        if self.head == None:
            return False
        
        return self.search_element(self.head, element)
    
l_list = LinkedList()

while True:
    print('\n1. Add a node.')
    print('2. Search element.')
    print('3. Exit.\n')

    choice = int(input("Enter the choice:- "))

    if choice == 1:
        data = int(input("\nEnter the value:- "))
        l_list.add_node(data)
    
    elif choice == 2:
        l_list.traverse()
        element = int(input('\nEnter value to be searched:- '))
        print(l_list.get_element())
    
    elif choice == 3:
        break
