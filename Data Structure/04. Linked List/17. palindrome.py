'''
To check whether a linked list is palindrome or not.
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
        Function to initialize LinkedList class object.

        Argument:
        self -- represents the object of the class.
        '''
        self.head = None
    
    def insert(self, data):
        '''
        Function to insert the node in the linked list.

        Arguments:
        self -- represents the object of the class.
        data -- int, data to be added to the node of the linked list.
        '''
        if self.head == None:
            ## if the linked list is empty
            self.head = Node(data)
            return
        
        head_pointer = self.head
        
        while head_pointer.next != None:
            head_pointer = head_pointer.next
        
        head_pointer.next = Node(data)
    
    def display(self):
        '''
        Function to display the linked list.

        Argument:
        self -- represents the object of the class.
        '''
        if self.head == None:
            ## if the linked list is empty
            return
        
        head_pointer = self.head

        while head_pointer != None:
            print(head_pointer.data, end=' ')
            head_pointer = head_pointer.next
        print()

    def find_middle(self):
        '''
        Function to find the middle element in the linked list.

        Argument:
        self -- represents the object of the class.

        Returns:
        int, middle element position.
        '''
        if self.head == None:
            ## if linked list is empty
            return
        
        fast_pointer = self.head
        slow_pointer = self.head

        while fast_pointer != None and fast_pointer.next != None:
            fast_pointer = fast_pointer.next.next

            if fast_pointer == None:
                return slow_pointer

            slow_pointer = slow_pointer.next
        
        return slow_pointer
    
    def is_palindrome(self, mid_node):
        '''
        Function to check wheter the given middle element is a palindrome or not.

        Arguments:
        self -- represents the object of the class.
        mid_node -- node class object, rerpesenting the middle element.

        Returns:
        bool -- True, if the linked list is palindrome.
                False, otherwise
        '''
        head_pointer = self.head
        reverse_pointer = mid_node.next

        while reverse_pointer != None:
            if head_pointer.data == reverse_pointer.data:
                head_pointer = head_pointer.next
                reverse_pointer = reverse_pointer.next
            else:
                return False
        
        return True
    
def reverse(node):
    '''
    Function to reverse the linked list.

    Argument:
    node -- node class object    
    '''
    if node == None:
        ## if the node is empty
        return

    current = node.next
    prev = None
    nxt = None

    while current != None:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    
    node.next = prev
    
l_list = LinkedList()

while True:
    print()
    print('1. Add node to linked list.')
    print('2. Display linked list.')
    print('3. Is palindrome.')
    print('4. Exit')

    choice = int(input('Enter your choice:- '))
    print()

    if choice == 1:
        data = input('Enter the data:- ')
        l_list.insert(data)

    elif choice == 2:
        l_list.display()
    
    elif choice == 3:
        node = l_list.find_middle()
        reverse(node)
        value = l_list.is_palindrome(node)
        print(value)

    elif choice == 4:
        break
