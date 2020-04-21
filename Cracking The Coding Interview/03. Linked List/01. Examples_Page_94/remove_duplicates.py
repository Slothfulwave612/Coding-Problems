'''
Remove Dups: Write code to remove duplicates from an unsorted linked list.

For Follow Up: The time complexity will be O(N^2), as we will take two 
pointers first will track one number another will see whether this number
is present in the rest of the list or not.
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
        data -- int, the data to be added to the node.
        '''
        self.data = data
        self.next = None
    
class LinkedList:
    '''
    a linked list class.
    '''

    def __init__(self):
        '''
        Function to initialize the LinkedList class object.

        Arguments:
        self -- represents the object of the class.
        '''
        self.head = None
    
    def add_node(self, data):
        '''
        Function to add node to the linked list.

        Arguments:
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
    
    def remove_duplicates(self):
        '''
        Function to remove duplicates from a linked list.

        Argument:
        self -- represents the object of the class.
        '''
        if self.head == None:
            ## if linked list is empty
            return
        
        hash_map = {}
        temp = self.head
        hash_map[temp.data] = 1

        while temp.next != None:
            if hash_map.get(temp.next.data) == 1:
                ## delete the node
                del_node = temp.next
                temp.next = del_node.next
                del del_node
            else:
                hash_map[temp.next.data] = 1
                temp = temp.next

l_list = LinkedList()

while True:
    print('1. Add a node.')
    print('2. Remove Duplicates')
    print('3. Exit')

    choice = int(input("Enter the choice:- "))

    if choice == 1:
        data = int(input("Enter the data:- "))
        l_list.add_node(data)
    
    elif choice == 2:
        l_list.traverse()
        l_list.remove_duplicates()
        l_list.traverse()
    
    elif choice == 3:
        break
