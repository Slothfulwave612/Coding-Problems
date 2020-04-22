'''
Palindrome: Implement a function to check if a linked list is a palindrome. 
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
        Function to initialize the Linked List class objects.

        Arguments:
        self -- represents the object of the class.
        '''
        self.head = None
    
    def add_node(self, data):
        '''
        Function to add node to the linked list.

        Argument:
        self -- represents the object of the class.
        data -- int, data to be added to the node.
        '''
        if self.head == None:
            ## if linked list is empty
            self.head = Node(data)
            return
        
        temp = self.head
        while temp.next != None:
            print(temp.data, end=' ')
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
    
    def is_palindrome(self):
        '''
        Function to check whether a given linked list is a palindrome or not.

        Argument:
        self -- represents the object of the class.

        Returns:
        True -- if it is palindrome
        False -- if not
        '''
        if self.head == None:
            ## if linked list is empty
            return
        
        stack = []

        temp = self.head

        while temp != None:
            if len(stack) == 0:
                stack.append(temp.data)
            elif temp.data == stack[-1]:
                stack.pop()
            else:
                stack.append(temp.data)
            
            temp = temp.next
        
        if len(stack) == 0:
            return True
        else:
            return False
    
l_list = LinkedList()

while True:
    print()
    print('1. Add a node')
    print('2. Traverse the linked list.')
    print('3. Is Palindrome')
    print('4. Exit')

    choice = int(input("Enter Your Choice"))
    print()

    if choice == 1:
        data = input("Enter Data:- ")
        l_list.add_node(data)
    
    elif choice == 2:
        l_list.traverse()
    
    elif choice == 3:
        print(l_list.is_palindrome())
    
    elif choice == 4:
        break
