'''
Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
'''

class Stack:
    '''
    a stack min.
    '''

    def __init__(self):
        '''
        Function to initilize Stack class objects.

        Argument:
        self -- represents the object of the class.
        '''
        self.stack = []
        self.supp_stack = []        ## supporting stack
    
    def push(self, data):
        '''
        Function will push the data into stack.

        Arguments:
        self -- represents the object of the class.
        data -- int, data to be added to the stack.
        '''
        if len(self.stack) == 0:
            self.supp_stack.append(data)
        
        elif data < self.supp_stack[-1]:
            self.supp_stack.append(data)
        self.stack.append(data)
    
    def pop(self):
        '''
        Function to remove the topmost element from the stack.

        Argument:
        self -- represents the object of the class.
        '''
        if len(self.stack) == 0:
            print('Stack Underflow')
            return
        
        if self.stack[-1] == self.supp_stack[-1]:
            self.supp_stack.pop()
        self.stack.pop()
    
    def getmin(self):
        '''
        Function to get minimum element from the stack.

        Argument:
        self -- represents the object of the class.

        Returns:
        minimum element.
        '''
        if len(self.stack) == 0:
            print('Stack Underflow')
            return
        
        return self.supp_stack[-1]
    
stack = Stack()

stack.push(5)
print(stack.getmin())
stack.push(1)
stack.push(2)
print(stack.getmin())
stack.push(10)
print(stack.getmin())

stack.pop()
print(stack.getmin())
stack.pop()
print(stack.getmin())
stack.pop()
print(stack.getmin())
