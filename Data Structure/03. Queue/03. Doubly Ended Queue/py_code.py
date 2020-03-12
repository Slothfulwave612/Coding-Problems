## Doubly Ended Queue

class deQueue:
    '''
    This class contains functions for doubly ended queue.
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
        self.queue = [0] * self.max_size
    
    def insert_rare(self, item):
        '''
        This function inserts at the rare position.

        Arguments:
        self -- represents the object of the class.
        item -- integer value, the value to be appended.
        '''
        if (self.front == 0 and self.rare == self.max_size - 1) or (self.front == self.rare + 1):
            print('Overflow')
        else:
            if self.front == -1:
                self.front = 0
                self.rare = 0
            elif self.rare == self.max_size - 1:
                self.rare = 0
            else:
                self.rare += 1
            
            self.queue[self.rare] = item
    
    def insert_front(self, item):
        '''
        This function inserts at the front position.

        Arguments:
        self -- represents the object of the class.
        item -- integer value, the value to be appended.
        '''
        if (self.front == 0 and self.rare == self.max_size - 1) or (self.front == self.rare + 1):
            print('Overflow')
        else:
            if self.front == -1:
                self.front = 0
                self.rare = 0
            elif self.front == 0:
                self.front = self.max_size - 1
            else:
                self.front -= 1
            
            self.queue[self.front] = item
        
    def remove_rare(self):
        '''
        This function removes from the rare position.

        Arguments:
        self -- represents the object of the class.
        '''
        if self.front == -1:
            print('Underflow')
        else:
            if self.rare == 0:
                self.rare = self.max_size - 1
            elif self.rare == self.front:
                self.rare = -1
                self.front = -1
            else:
                self.rare -= 1
    
    def remove_front(self):
        '''
        This function removes from the front position.

        Arguments:
        self -- represents the object of the class.
        '''
        if self.front == -1:
            print('Underflow')
        else:
            if self.front == self.max_size - 1:
                self.front = 0
            elif self.front == self.rare:
                self.front = -1
                self.rare = -1
            else:
                self.front += 1
    
    def display(self):
        '''
        This function will display the content of the queue.

        Argument:
        self -- represents the object of the class.
        '''
        if self.front == -1:
            print('Underflow')
        else:
            index = self.front
            while index != self.rare:
                print(self.queue[index], end=' ')
                index = (index + 1) % self.max_size
            print(self.queue[index])

obj = deQueue()

obj.insert_front(1)
obj.display()

obj.insert_rare(2)
obj.display()

obj.insert_rare(3)
obj.display()

obj.insert_front(0)
obj.display()

obj.insert_front(-1)
obj.display()

obj.insert_front(1)         ## Overflow
obj.display()

obj.remove_front()
obj.display()

obj.remove_front()
obj.display()

obj.remove_rare()
obj.display()

obj.remove_rare()
obj.display()

obj.remove_front()
obj.display()               ## Underflow

obj.remove_front()          ## Underflow
