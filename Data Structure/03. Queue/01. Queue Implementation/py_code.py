## Queue Implementation

class Queue:
    '''
    This class contains functions for queue data structure implementation.

    Enqueue: To add at rare position.
    Dequeue: To remove at front position.
    '''

    def __init__(self):
        '''
        Constructor function.

        Argument:
        self -- represents the object of the class.
        '''
        self.queue = []
        self.front = None
        self.rare = None
        self.max_size = 5
    
    def enqueue(self, item):
        '''
        This function will add the item to the queue.

        Argument:
        self -- represents the object of the class.
        item -- integer value.
        '''
        if self.rare == self.max_size - 1:
            print('Overflow')
        else:
            self.queue.append(item)
            if self.front == None:
                self.front = 0
                self.rare = 0
            else:
                self.rare += 1
    
    def dequeue(self):
        '''
        This function will remove the element from the queue.

        Argument:
        self -- represents the object of the class.
        '''
        if self.front == None:
            print('Underflow')
        else:
            self.front += 1
            if self.front > self.rare:
                self.front = None
                self.rare = None
    
    def display(self):
        '''
        This function will display the content of the queue.

        Argument:
        self -- represents the object of the class.
        '''
        if self.front == None:
            print('Underflow')
        else:
            for i in range(self.front, self.rare + 1):
                print(self.queue[i], end=' ')
            print()

obj = Queue()

obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
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
