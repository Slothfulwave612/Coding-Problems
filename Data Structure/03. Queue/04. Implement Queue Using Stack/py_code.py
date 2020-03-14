## Implement Queue Using Stack

class Stack:
    '''
    This class contains function for queue implementation using stack
    '''

    def __init__(self):
        '''
        Constructor function.

        Argument:
        self -- represents the object of the class.
        '''
        self.stack = []
        self.stack_2 = []
        self.max_size = 5

    def push(self, item):
        '''
        This function inserts the element into the queue.

        Argument:
        self -- represents the object of the class.
        item -- integer value, represents the value to be inserted.
        '''
        while self.stack != []:
            self.stack_2.append(self.stack.pop())
            
        self.stack.append(item)

        while self.stack_2 != []:
            self.stack.append(self.stack_2.pop())
    
    def Pop(self):
        '''
        This function will remove the front element.

        Argument:
        self -- represents the obejct of the class.
        '''
        if len(self.stack) == 0:
            print('Underflow')
        else:
            self.stack.pop()
    
    def display(self):
        '''
        This function will show all the content of the stack.

        Argument:
        self -- represents the object of the class.
        '''
        if self.stack == []:
            print('Underflow')
        else:
            for i in range(len(self.stack) - 1, -1, -1):
                print(self.stack[i], end=' ')
            print()

obj = Stack()

obj.push(1)
obj.display()

obj.push(2)
obj.display()

obj.push(3)
obj.display()

obj.push(4)
obj.display()

obj.push(5)
obj.display()

obj.Pop()
obj.display()

obj.Pop()
obj.display()

obj.Pop()
obj.display()

obj.Pop()
obj.display()

obj.Pop()

obj.display()       ## Underflow
obj.Pop()           ## Underflow
