'''
Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).Thatis,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
'''

class Node:
    '''
    a node class.
    '''

    def __init__(self, data):
        '''
        Function to initialize the object of Node class.

        Arguments:
        self -- represents the object of the class.
        data -- int, data to be added to the linked list.
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
    
    def add_node(self, data):
        '''
        Function to add node to linked list.

        Arguments:
        self -- represents the object of the class.
        data -- int, the data to be added to the node.
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
    
    def sum_lists(self, l_list2):
        '''
        Function to sum the two list and append result in third.

        Arguments:
        self -- represents the object of the class.
        l_list2 -- second linked list.

        Retunrs:
        l_list3 -- third linked list.
        '''
        if self.head == None or l_list2.head == None:
            ## if one of the linked list is empty
            return
        
        def reverse(num):
            '''
            Function will reverse the number.

            Argument:
            num -- int, the number to be reversed

            Returns:
            rev -- int, the reversed number.
            '''
            rev = 0
            while num > 0:
                rev = (rev * 10) + (num % 10)
                num = num // 10
            
            return rev

        num1 = 0
        temp = self.head

        while temp != None:
            num1 = (num1 * 10) + temp.data
            temp = temp.next
        
        num2 = 0
        temp = l_list2.head

        while temp != None:
            num2 = (num2 * 10) + temp.data
            temp = temp.next
        
        num1 = reverse(num1)
        num2 = reverse(num2)

        summ = num1 + num2
        l_list3 = LinkedList()

        while summ != 0:
            l_list3.add_node(summ % 10)
            summ = summ // 10
        
        return l_list3

l_list1 = LinkedList()
l_list2 = LinkedList()

l_list1.add_node(7)
l_list1.add_node(1)
l_list1.add_node(6)

l_list2.add_node(5)
l_list2.add_node(9)
l_list2.add_node(2)

l_list1.traverse()
print()
l_list2.traverse()

l_list3 = l_list1.sum_lists(l_list2)
l_list3.traverse()
