## Delete the first occurrence of this key in linked list.

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize the node class object.

        Arguments:
        self -- represents the object the class.
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
        Function to initialize object of linked list class.

        Argument:
        self -- represents the object of the class.
        '''
        self.head = None

    def add_node(self, data):
        '''
        Function will add node to the linked list.

        Arguments:
        self -- represents the object of the class.
        data -- int, values to be inserted in the node.
        '''
        if self.head == None:
            ## if linked list is empty
            self.head = Node(data)
        else:
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
        else:
            temp = self.head
            while temp != None:
                print(temp.data, end=' ')
                temp = temp.next
            print()
    
    def delete_node(self, key):
        '''
        Function to delete the first occurence of the key from linked list.

        Arguments:
        self -- represents the object of the class.
        key -- int, the key to be deleted from the linked list.
        '''
        if self.head == None:
            return 
        else:
            if self.head.next == None and self.head.data == key:
                self.head = None
                return
            elif self.head.next == None and self.head.data != key:
                print('Key not found')
                return

            temp = self.head
            while temp.next.data != key:
                temp = temp.next
                if temp.next == None:
                    print('Key not found')
                    return
            
            temp.next = temp.next.next

l_list = LinkedList()

while True:
    print('\n1. Insert a Node.')
    print('2. Delete a Node.')
    print('3. Exit.')

    choice = int(input("Enter the choice:- "))

    if choice == 1:
        data = int(input('\nEnter a value:- '))
        l_list.add_node(data)
    
    elif choice == 2:
        l_list.traverse_node()
        key = int(input("\nProvide a key:- "))
        print()
        l_list.delete_node(key)
        print()
        l_list.traverse_node()
    
    elif choice == 3:
        break
