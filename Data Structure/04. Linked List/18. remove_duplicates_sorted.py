## Removes duplicates from a sorted linked list.

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize the Node class objects.

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
        Function to initialize the LinkedList object.

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
    
    def remove_duplicates(self):
        '''
        Function removes duplicates from the linked list.

        Argument:
        self -- represents the object of the class.
        '''
        if self.head == None:
            ## if the linked list is empty
            return
        
        temp = self.head
        prev_data = temp.data

        while temp.next != None:
            if temp.next.data == prev_data:
                ## if duplicate is found
                del_node = temp.next
                temp.next = del_node.next
                del del_node
            else:
                prev_data = temp.next.data
                temp = temp.next

l_list = LinkedList()

while True:
    print('\n1. Add a node.')
    print('2. Traverse linked list.')
    print('3. Remove duplicates.')
    print('4. Exit.\n')

    choice = int(input("Enter a choice:- "))

    if choice == 1:
        data = int(input("\nEnter data:- "))
        l_list.add_node(data)
    
    elif choice == 2:
        l_list.traverse()
    
    elif choice == 3:
        l_list.remove_duplicates()
    
    elif choice == 4:
        break
