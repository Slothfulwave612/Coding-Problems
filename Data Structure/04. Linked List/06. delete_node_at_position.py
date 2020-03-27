## Delete a Linked List node at a given position

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize node class objects.

        Arguments:
        self -- represents the obeject of the class.
        data -- int, values to be inserted in the node.
        '''
        self.data = data
        self.next = None

class LinkedList:
    '''
    a linked list class.
    '''

    def __init__(self):
        '''
        Function to initialize the object of node class.

        Argument:
        self -- represents the object of the class.
        '''
        self.head = None

    def add_node(self, data):
        '''
        Function to add node to the linked list.

        Arguments:
        self -- represents the object of the class.
        data -- int, values to be added to the node.
        '''
        if self.head == None:
            ## if linked list is empty
            self.head = Node(data)
        else:
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
            print('Empty Linked List')
        else:
            temp = self.head
            while temp != None:
                print(temp.data, end=' ')
                temp = temp.next
            print()
    
    def delete_pos_node(self, pos):
        '''
        Function to delete the node at a given position.

        Arguments:
        self -- represents the object of the class.
        pos -- int, positional value of the node to be deleted.
        '''
        if self.head == None:
            print('Empty Linked List')
        else:
            temp = self.head
            count = 0
            
            if pos == 0:
                self.head = self.head.next
                temp = None
                return

            while count != pos - 1:
                temp = temp.next
                if temp == None:
                    print('No Node found')
                    return
                count += 1
            
            if temp.next == None:
                print('No node found')
                return

            del_node = temp.next
            temp.next = temp.next.next
            del_node = None

l_list = LinkedList()

while True:
    print('\n1. Insert a node.')
    print('2. Delete a node.')
    print('3. Exit\n')

    choice = int(input("Enter a choice:- "))

    if choice == 1:
        data = int(input("Enter a value:- "))
        l_list.add_node(data)
    
    elif choice == 2:
        l_list.traverse()
        print()

        pos = int(input("Enter a position:- "))
        l_list.delete_pos_node(pos)
        print()
        l_list.traverse()
    
    elif choice == 3:
        break
