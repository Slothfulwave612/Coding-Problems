'''
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
'''

class Stack:
    '''
    a stack class.
    '''

    def __init__(self):
        '''
        Function to initialize the Stack class objects.

        Argument:
        self -- represents the object of the class.
        '''
        self.stack_1 = []
        self.stack_2 = []
    
    def push(self, data):
        '''
        Function to push the item to the stack.

        Arguments:
        self -- represents the object of the class.
        data -- int, the data to be added to the stack.
        '''
        self.stack_1.append(data)
    
    def pop(self):
        '''
        Function to remove the item from the stack.

        Argument:
        self -- represents the object of the class.
        '''
        if self.stack_1 == []:
            print('Stack Underflow')
            return
        
        while len(self.stack_1) != 1:
            self.stack_2.append(self.stack_1.pop())
        
        self.stack_1.pop()
    
        while self.stack_2 != []:
            self.stack_1.append(self.stack_2.pop())
        
    def display(self):
        '''
        Function to display the stack.

        Argument:
        self -- represents the object of the class.
        '''
        if self.stack_1 == []:
            print('Stack Underflow')
            return
        
        print(self.stack_1)
    
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

stack.display()

stack.pop()
stack.display()
stack.pop()
stack.display()
stack.pop()
stack.display()
stack.pop()
stack.display()
stack.pop()
stack.display()
stack.pop()
