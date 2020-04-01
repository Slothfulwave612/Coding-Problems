## Remove duplicates from an unsorted linked list.

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize Node class objects.

        Arguments:
        self -- represents the object of the class.
        data -- int, value to be added to the node.
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

        Arguments:
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
    
    def remove_duplicates(self):
        '''
        Function to remove the duplicates from the linked list.

        Argument:
        self -- represents the object of the class.
        '''
        if self.head == None:
            ## if linked list is empty
            return
        
        hash_table = {}
        temp = self.head
        hash_table[temp.data] = 1

        while temp.next != None:
            if hash_table.get(temp.next.data) == True:
                del_node = temp.next
                temp.next = del_node.next
                del del_node
            else:
                hash_table[temp.next.data] = 1
                temp = temp.next

l_list = LinkedList()

while True:
    print('\n1. Add a node.')
    print('2. Traverse the linked list.')
    print('3. Remove duplicates.')
    print('4. Exit.\n')

    choice = int(input("Enter choice:- "))

    if choice == 1:
        data = int(input("Enter data:- "))
        l_list.add_node(data)
    
    elif choice == 2:
        l_list.traverse()
    
    elif choice == 3:
        l_list.remove_duplicates()
    
    elif choice == 4:
        break
