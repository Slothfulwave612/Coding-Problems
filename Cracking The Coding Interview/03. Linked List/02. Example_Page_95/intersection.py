'''
Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting. 
'''

class Node:
    '''
    a node class.
    '''

    def __init__(self):
        '''
        Function to initialize the Node class objects.

        Arguments:
        self -- represents the object of the class.
        data -- int, data to be added to the node.
        '''
        self.data = None
        self.next = None
    
def traverse(l_list):
    '''
    Function to traverse the linked list.

    Argument:
    l_list -- linked list head.
    '''
    if l_list == None:
        ## if linked list is empty
        return
    
    temp = l_list

    while temp != None:
        print(temp.data, end=' ')
        temp = temp.next
    print()

def intersection(l_list1, l_list2):
    '''
    Function to find the intersection of the linked list.

    Argument:
    l_list1 -- first linked list head.
    l_list2 -- second linked list head.

    Returns:
    the intersection data if found else False
    '''
    if l_list1 == None or l_list2 == None:
        ## if linked list is empty
        return
    
    hash_table = {}
    temp = l_list1

    while temp != None:
        hash_table[temp] = True
        temp = temp.next
    
    temp = l_list2
    while temp != None:
        if hash_table.get(temp) == True:
            print(temp.data)
            return
        temp = temp.next
    
    return False

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

traverse(head1)
traverse(head2)

intersection(head1, head2)
