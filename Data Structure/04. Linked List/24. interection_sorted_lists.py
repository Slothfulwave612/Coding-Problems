## Intersection of two Sorted Linked Lists.

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
        Function to initialize LinkedList class objects.

        Argument:
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
        self -- represents the class of the class.
        '''
        if self.head == None:
            ## if linked list is empty
            print('yes')
            return
        
        temp = self.head
        
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        print()
    
    def intersection(self, second_list):
        '''
        Function to find the intersection data and make a new linked list

        Arguments:
        self -- represents the object of the class.
        second_list -- linked list

        Returns:
        third_list -- the linked list formed after finding intersection points.
        '''
        if self.head == None or second_list.head == None:
            ## if any linked list is empty
            return
        
        a = self.head
        b = second_list.head
        third_list = LinkedList()
        
        while a != None and b != None:
            if a.data == b.data:
                third_list.add_node(a.data)
                a = a.next
                b = b.next
            
            elif a.data < b.data:
                a = a.next
            
            elif b.data > a.data:
                b = b.next
        
        return third_list
    
l_list_1 = LinkedList()
l_list_2 = LinkedList()

l_list_1.add_node(1)
l_list_1.add_node(2)
l_list_1.add_node(3)
l_list_1.add_node(4)
l_list_1.add_node(5)
l_list_1.add_node(6)

l_list_2.add_node(2)
l_list_2.add_node(4)
l_list_2.add_node(6)
l_list_2.add_node(8)

l_list_3 = l_list_1.intersection(l_list_2)

l_list_3.traverse()
