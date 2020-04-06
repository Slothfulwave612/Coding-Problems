## Write a function to get the intersection point of two Linked Lists

class Node:
    '''
    a node class.
    '''

    def __init__(self):
        '''
        Function to initialize the Node class objects.

        Arguments:
        self -- represents the object of the class.
        '''
        self.data = None
        self.next = None
    
def find_intersection(first_list, second_list):
    '''
    Function finds the interection between two linked list.

    Arguments:
    first_list -- linked list.
    second_list -- linked list.

    Returns:
    int, data value of intersecting node.
    '''
    if first_list == None or second_list == None:
        ## if linked list is empty
        return
    
    a = first_list
    b = second_list

    while a != b:
        if a == None:
            a = second_list
        else:
            a = a.next
        
        if b == None:
            b = first_list
        else:
            b = b.next
        
    return a.data

newNode = None
head1 = Node() 
head1.data = 10
head2 = Node() 
head2.data = 3
newNode = Node() 
newNode.data = 6
head2.next = newNode 
newNode = Node() 
newNode.data = 9
head2.next.next = newNode 
newNode = Node() 
newNode.data = 15
head1.next = newNode 
head2.next.next.next = newNode 
newNode = Node() 
newNode.data = 30
head1.next.next = newNode 
head1.next.next.next = None
  
# Print the intersection node 
print(find_intersection(head1, head2))
