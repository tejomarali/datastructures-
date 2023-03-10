" Create a queue and perform various operations on it:"
class queue:
    def __init__(self, max_size, size=0, front=0, rear=0):
        self.queue = [[] for i in range(5)] #creates a list [0,0,0,0,0]
        self.max_size = max_size
        self.size = size
        self.front = front
        self.rear = rear
    def enqueue(self, data): 
        if not self.isFull():
            self.queue[self.rear] = data
            self.rear = int((self.rear + 1) % self.max_size)
            self.size += 1
        else:
            print('Queue is full')
    def dequeue(self): 
        if not self.isEmpty():
            print(self.queue[self.front], 'is removed')
            self.front = int((self.front + 1) % self.max_size)
            self.size -= 1
        else:
            print('Queue is empty')
    def isEmpty(self): 
        return self.size == 0
    def isFull(self): 
        return self.size == self.max_size
    def show(self):
        print ('Queue contents are:')
        for i in range(self.size):
            print (self.queue[int((i+self.front)% self.max_size)])
q = queue(5)
print('Queue Insertion')
q.enqueue(1)
q.show()
q.enqueue(2)
q.show()
q.enqueue(3)
q.show()
q.enqueue(4)
q.show()
q.enqueue(5)
q.show(
print('Queue Deletion'))
q.dequeue()
q.show()
q.dequeue()
q.show()
q.dequeue()
q.show()
q.dequeue()
q.show()
q.dequeue()
q.show()


OUTPUT:-
Queue Insertion
Queue contents are:
1
Queue contents are:
1
2
Queue contents are:
1
2
3
Queue contents are:
1
2
3
4
Queue contents are:
1
2
3
4
5
Queue Deletion
1 is removed
Queue contents are:
2
3
4
5
2 is removed
Queue contents are:
3
4
5
3 is removed
Queue contents are:
4
5
4 is removed
Queue contents are:
5
5 is removed
Queue contents are:
