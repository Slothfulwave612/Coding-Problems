## Implementing Stack Using Queues

class Stack:
    '''
    This class contains methods for implementation of stack using Queue data structure.
    '''

    def __init__(self):
        '''
        Constructor function.

        Argument:
        self -- represents the object of the class.
        '''
        self.queue = []
        self.queue_2 = []
        self.top = -1
        self.max_size = 5

    def enqueue(self, item):
        '''
        This function will append item to the stack.

        Arguments:
        self -- represents the object of the class.
        item -- integer value to be appended to the stack.
        '''
        if self.top == self.max_size - 1:
            print('Stack Overflow')
        else:
            self.top += 1

            self.queue_2.append(item)

            while self.queue_2 != []:
                pop_item = self.queue_2.pop()
                self.queue.append(pop_item)
    
    def dequeue(self):
        '''
        This function will remove the topmost element from the stack.

        Argument:
        self -- represents the object of the class.
        '''
        if self.queue == []:
            print('Underflow')
        else:   
            self.queue.pop()
            self.top -= 1
    
    def display(self):
        '''
        This function will display the content of the stack.

        Argument:
        self -- represents the object of the class.
        '''
        if self.queue == []:
            print('Underflow')
        else:
            for i in range(self.top, -1, -1):
                print(self.queue[i], end=' ')
            print()

obj = Stack()

obj.enqueue(1)
obj.display()

obj.enqueue(2)
obj.display()

obj.enqueue(3)
obj.display()

obj.enqueue(4)
obj.display()

obj.enqueue(5)
obj.display()

obj.enqueue(6)      ## Overflow

obj.dequeue()
obj.display()

obj.dequeue()
obj.display()

obj.dequeue()
obj.display()

obj.dequeue()
obj.display()

obj.dequeue()

obj.display()       ## Underflow
obj.dequeue()       ## Underflow
