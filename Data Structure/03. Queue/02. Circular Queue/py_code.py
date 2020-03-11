## Circular Queue Implementation

class cQueue:
    '''
    This class contains functions for circular queue implementation.

    Rare: next_rare_value = (rare + 1) % max_size
    Front: next_front_value = (front + 1) % max_size
    Overflow: if front == (rare + 1) % max_size
    Underflow: if front == None
    '''

    def __init__(self):
        '''
        Constructor function.

        Argument:
        self -- represents the object of the class.
        '''
        self.front = -1
        self.rare = -1
        self.max_size = 5
        self.cqueue = [0] * self.max_size
    
    def enqueue(self, item):
        '''
        This function will add elements to the circular queue.

        Arguments:
        self -- represents the object of the class.
        item -- integer value to be appended on the queue.
        '''
        if self.front == (self.rare + 1) % self.max_size:
            print('Overflow')
        else:
            if self.front == -1:
                self.front += 1
                self.rare += 1
            else:
                self.rare = (self.rare + 1) % self.max_size
            self.cqueue[self.rare] = item
    
    def dequeue(self):
        '''
        This function removes the elements from the queue.

        Argument:
        self -- represnts the object of the class.
        '''
        if self.front == -1:
            print('Underflow')
        else:
            if self.front == self.rare:
                self.front = -1
                self.rare = -1
            else:
                self.front = (self.front + 1) % self.max_size
            print(self.front, self.rare)
    def display(self):
        '''
        This function displays the elements of the queue.

        Argument:
        self -- represents the object of the class.
        '''
        if self.front == -1:
            print('Underflow')
        else:
            index = self.front
            while index != self.rare:
                print(self.cqueue[index], end=' ')
                index = (index + 1) % self.max_size
            print(self.cqueue[index])

obj = cQueue()

obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)

obj.display()

obj.enqueue(6)       ## Overflow

obj.dequeue()
obj.enqueue(6)
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

obj.display()       ## Underflow
obj.dequeue()       ## Underflow
