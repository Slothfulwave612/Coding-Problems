## Priority Queue Implementation

class PriorityQueue:
    '''
    Priority Queue is an extension of the queue with following properties:
    1) An element with high priority is dequeued before an element with low priority.
    2) If two elements have the same priority, they are served according to their order in the queue.

    This class contains functions for priority queue operations.
    ''' 

    def __init__(self):
        '''
        Constructor Function.

        Argument:
        self -- represents the object of the class.
        '''
        self.queue = []
    
    def __str__(self):
        '''
        Used for string representation of the object.

        Argument:
        self -- represents the object of the class.

        Returns:
        elements of the queue.
        '''
        return ' '.join(str(elem) for elem in self.queue)

    def is_Empty(self):
        '''
        For checking whether the queue is empty or not.

        Argument:
        self -- represents the object of the class

        Return:
        bool value -- True: if empty
                      False: otherwise
        '''
        return self.queue == []
    
    def insert(self,item):
        '''
        For inserting the item into the queue.

        Arguments:
        self -- represents the object of the class.
        item -- int, item to be inserted.
        '''
        self.queue.append(item)
    
    def delete(self):
        '''
        For deleting the value from the queue.

        Argument:
        self -- represents the object of the class.

        Returns:
        item -- int, the item deleted.
        '''
        try:
            maxim = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[maxim]:
                    maxim = i
            item = self.queue[maxim]
            del self.queue[maxim]
            return item
        except IndexError:
            print()
            exit()

Queue = PriorityQueue()

Queue.insert(12)
Queue.insert(1)
Queue.insert(14)
Queue.insert(7)

print(Queue)

while Queue.is_Empty() == False:
    print(Queue.delete())
