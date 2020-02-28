## Stack Implementation

class Stack:
    '''
    The class Stack contains all the helper functions for stack implementation.
    '''

    def __init__(self):
        '''
        Arguments:
        self -- reference to the object.
        '''
        self.stack = []
        self.max_size = 5
        self.top = 0

    def push(self, item):
        '''
        The function will push the required item to the stack.

        Arguments:
        self -- reference to the object.
        item -- item to be pushed.
        '''
        
        if self.top == self.max_size:
            print('Stack Overflow\n')
        
        else:
            self.stack.append(item)
            self.top += 1
    
    def pop(self):
        '''
        The function will pop the topmost item from the stack.

        Arguments:
        self -- reference to the object.
        '''

        if self.top == 0:
            print('Stack Underflow\n')
        
        else:
            self.stack.pop()
            self.top -= 1
    
    def display_stack(self):
        '''
        The function will display the items present in the stack.

        Arguments:
        self -- reference to the object.
        '''

        if self.top == 0:
            print('Stack Underflow\n')
        
        else:
            for item in range(self.top - 1, -1, -1):
                print(self.stack[item], end=' ')
            print()

stack = Stack()     ## creating object of class Stack

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

stack.push(6)           ## Overflow condition
        
stack.display_stack()   ## 5 4 3 2 1

stack.pop()
stack.pop()
stack.pop()

stack.display_stack()   ## 2 1

stack.pop()
stack.pop()

stack.pop()             ## Underflow condition

stack.display_stack()   ## Underflow condition
