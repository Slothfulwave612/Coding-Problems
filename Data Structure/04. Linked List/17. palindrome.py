## Check if a linked list of strings forms a palindrome.

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize the Node class objects.

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
        Function to initialize the Linked List object.

        Argument:
        self -- represents the object of the class.
        '''
        self.head = None
    
    def is_palindrome(self):
        '''
        Function to check for palindrome.

        Argument:
        self -- represents the object of the class.
        '''
        string = ''

        temp = self.head
        while temp != None:
            string += temp.data
            temp = temp.next
        
        return string == string[::-1]

llist = LinkedList() 
llist.head = Node('a') 
llist.head.next = Node('bc') 
llist.head.next.next = Node("d") 
llist.head.next.next.next = Node("dcb") 
llist.head.next.next.next.next = Node("a") 
print(True if llist.is_palindrome() else False)

