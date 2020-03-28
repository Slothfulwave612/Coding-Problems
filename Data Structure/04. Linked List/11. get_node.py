## Get nth node of the linked list.

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize the object of Node class.

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

        Argument:
        self -- represents the object of the class.
        '''
        self.head = None

    def add_node(self, data):
        '''
        Function to add node to the linked list.

        Argument:
        self -- represents the object of the class.
        data -- int, value to be inserted in the node.
        '''
        if self.head == None:
            ## is the linked list is empty
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
            ## if the linked list is empty
            return 
        
        temp = self.head
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        print()
    
    def get_node(self, pos):
        '''
        Function to get the node at specified position.

        Arguments:
        self -- represents the object of the class.
        pos -- int, representing the position of the node.

        Returns:
        temp.data -- int, returns the data at that particular node.
        '''
        if self.head == None:
            ## if linked list is empty
            return
        
        count = 0
        temp = self.head

        while count != pos:
            temp = temp.next
            if temp == None:
                break
            count += 1
        else:
            return temp.data

l_list = LinkedList()

while True:
    print('\n1. Add a node.')
    print('2. Get node.')
    print('3. Exit.\n')

    choice = int(input("Enter the choice:- "))

    if choice == 1:
        data = int(input("Enter the data:- "))
        l_list.add_node(data)
    
    elif choice == 2:
        l_list.traverse()
        pos = int(input("\nEnter position:- "))
        print(l_list.get_node(pos))
    
    elif choice == 3:
        break
